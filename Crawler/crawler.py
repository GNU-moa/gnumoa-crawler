import requests
from bs4 import BeautifulSoup
from .firebase import db
from datetime import datetime
from .sendUpdata import send_push_notification


class Crawler:
    def __init__(self,
                 departmentCollege,
                 departmentName_ko,
                 departmentName_en,
                 categoryTags):
        self.departmentCollege = departmentCollege
        self.departmentName_ko = departmentName_ko
        self.departmentName_en = departmentName_en
        self.categoryTags = categoryTags

    def getBaseUrls(self): #공지사항 url 반환
        baseUrls = []
        categoryNames = []
        for categoryTag in self.categoryTags:
            categoryName = categoryTag[0]
            mi = categoryTag[1]
            bbsId = categoryTag[2]
            baseUrl = f'https://www.gnu.ac.kr/{self.departmentName_en}/na/ntt/selectNttList.do?mi={mi}&bbsId={bbsId}'
            baseUrls.append(baseUrl)
            categoryNames.append(categoryName)
        return categoryNames, baseUrls

    def do_html_crawl(self, Url): #웹 페이지의 html내용 가져오기
        request = requests.get(Url)
        parsed_html = BeautifulSoup(request.text, 'html.parser')
        return parsed_html

    def division_postInfo(self, baseUrl): #필수 공지 및 일반 공지 구분
        parsed_html = self.do_html_crawl(baseUrl)
        getNums = parsed_html.find_all('b', {'class': 'btn_S btn_default'})

        getDivision = parsed_html.select('div.BD_list > table > tbody > tr:nth-child(' + str(len(getNums)+1)  + ') > td:nth-child(1)')

        if (len(getDivision) == 0):
            division = 0
        else:
            division = getDivision[0].text.strip()

        GetDataWords = parsed_html.find_all('a', {'class': 'nttInfoBtn'})

        GetDataIds = []
        for Word in GetDataWords:
            GetDataIds.append(Word['data-id'])

        return len(getNums), GetDataIds, division

    def get_posts(self, CountIndex, baseUrl, GetDataIds): #구분된 공지 url들 구하기
        get_essential_posts = []
        for i in range(CountIndex):
            postUrl = f'{baseUrl.replace("selectNttList", "selectNttInfo")}&nttSn={GetDataIds[i]}'
            get_essential_posts.append(postUrl)

        getPostUrls = []
        for i in range(CountIndex, CountIndex + 10):
            try:
                postUrl = f'{baseUrl.replace("selectNttList", "selectNttInfo")}&nttSn={GetDataIds[i]}'
                getPostUrls.append(postUrl)
            except IndexError: # 게시판에 게시물이 10개 미만일 경우
                pass
        return get_essential_posts, getPostUrls


    def save_url_Info(self, doc_ref, parsed_html, post_url, categoryName): #공지 정보 firebase에 저장 및 안드로이드 push 기능
        createdAt_string = parsed_html.select_one('div.BD_table > table > tbody > tr:nth-child(3) > td').text
        #작성자 없을 때 예외처리
        if (len(createdAt_string) != 10):
            createdAt_string = parsed_html.select_one('div.BD_table > table > tbody > tr:nth-child(2) > td').text
        if createdAt_string[:4] != '2023':
            return

        title = parsed_html.find("th", class_="title")
        if title:
            title = title.get_text(strip=True)
        else:
            title = ''

        print(self.departmentName_en + " " + categoryName + " : " + title)

        get_imgs = parsed_html.find_all('img')

        for img in get_imgs:
            if not img['src'].startswith('https'):
                img['src'] = 'https://www.gnu.ac.kr' + img['src']

            img.attrs['style'] = 'width:100%'


        contents = parsed_html.find_all('tr', class_='cont')

        getHtml = str(contents)

        contents_texts = [c.text.strip() for c in contents]

        ul_file = parsed_html.find('ul', {'class': 'file'})
        li_tags = ul_file.find_all('li')

        links = {}
        for li in li_tags:
            a_tag = li.find('a')
            if a_tag is not None:
                for tag in a_tag.find_all():
                    tag.decompose()

                linkName = a_tag.text.strip()
                linkUrl = a_tag.get('href')

                links[linkName] = 'https://www.gnu.ac.kr' + linkUrl

        createdAt = datetime.strptime(createdAt_string, '%Y.%m.%d')

        post_info = {
            'title': title,
            'baseUrl': post_url,
            'html': getHtml[1: -1],
            'context' : [contents_texts[0][:90]],
            'fileUrls': links,
            'createdAt': createdAt,
            'major' : self.departmentName_ko,
            'category' : categoryName
        }
        doc_ref.set(post_info)

        tokens_ref = db.collection("Tokens")
        docs = tokens_ref.get()
        for doc in docs:
            field_keys = doc.to_dict().keys()
            for field_key in field_keys:
                chk = db.collection("Tokens").document(doc.id).get().to_dict()
                if("" != chk.get(field_key) and field_key == self.departmentName_ko):
                    send_push_notification(doc.id, self.departmentName_ko, categoryName, title)

    
    def save_essential_Info(self, categoryName, GetDataIds, get_essentialUrls): #업데이트 할 공지 구분하기 - 필수
        for i, post_url in enumerate(get_essentialUrls):
            doc_ref = db.collection(self.departmentCollege).document(self.departmentName_ko).collection(categoryName).document(GetDataIds[i])
            if doc_ref.get().exists:
                continue

            # 미래자동차공학과 비밀글
            if post_url == "https://www.gnu.ac.kr/car/na/ntt/selectNttInfo.do?mi=5865&bbsId=2131&nttSn=2117561":
                continue

            parsed_html = self.do_html_crawl(post_url)
            self.save_url_Info(doc_ref, parsed_html, post_url, categoryName)


    def save_basic_Info(self, categoryName, text, postUrls): #업데이트 할 공지 구분하기 - 일반
        for i, post_url in enumerate(postUrls):
            idx = str(int(text) - (len(postUrls) - 1) + i)
            doc_ref = db.collection(self.departmentCollege).document(self.departmentName_ko).collection(categoryName).document(idx)
            if doc_ref.get().exists:
                continue

            parsed_html = self.do_html_crawl(post_url)
            self.save_url_Info(doc_ref, parsed_html, post_url, categoryName)
