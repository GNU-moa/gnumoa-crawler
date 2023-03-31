import requests
from bs4 import BeautifulSoup
from .firebase import db
from datetime import datetime

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

    def do_html_crawl(self, Url):
        request = requests.get(Url)
        parsed_html = BeautifulSoup(request.text, 'html.parser')
        return parsed_html

    def get_posts(self, baseUrl):
        parsed_html = self.do_html_crawl(baseUrl)
        getNums = parsed_html.find_all('td', {'class': 'BD_tm_none'})
        CountIndex = 0  # 필독 공지 걸러내기
        for getNum in getNums:
            text = getNum.text.strip()
            if text != '공지':
                break
            CountIndex = CountIndex + 1
        GetDataWords = parsed_html.find_all('a', {'class': 'nttInfoBtn'})

        GetDataIds = []
        for Word in GetDataWords:
            GetDataIds.append(Word['data-id'])

        getPostUrls = []
        for i in range(CountIndex, CountIndex + 10):
            try:
                postUrl = f'{baseUrl.replace("selectNttList", "selectNttInfo")}&nttSn={GetDataIds[i]}'
                getPostUrls.append(postUrl)
            except IndexError: # 게시판에 게시물이 10개 미만일 경우
                pass

        return text, getPostUrls

    def get_title_and_context(self, categoryName, text, postUrls):
        post_info_list = []
        for i, post_url in enumerate(postUrls):
            # Url을 html로 변환
            parsed_html = self.do_html_crawl(post_url)

            idx = str(int(text) - (len(postUrls) - 1) + i)
            print(self.departmentName_en + '_' + categoryName + '_' + idx)
            doc_ref = db.collection(self.departmentCollege).document(self.departmentName_en).collection(categoryName).document(idx)
            if doc_ref.get().exists:
                continue

            title = parsed_html.find("th", class_="title")
            if title:
                title = title.get_text(strip=True)
            else:
                title = ''

            contents = parsed_html.find_all('tr', class_='cont')
            contents_texts = [c.text.strip() for c in contents]

            ul_file = parsed_html.find('ul', {'class': 'file'})
            li_tags = ul_file.find_all('li')

            links = []
            for li in li_tags:
                a_tag = li.find('a')
                if a_tag is not None:
                    link = a_tag.get('href')
                    links.append('https://www.gnu.ac.kr'+ link)
            
            createdAt_string = parsed_html.select_one('div.BD_table > table > tbody > tr:nth-child(3) > td').text
            createdAt = datetime.strptime(createdAt_string, '%Y.%m.%d')
            
            post_info = {
                'title': title,
                'baseUrl': post_url,
                'context': contents_texts,
                'fileUrls': links,
                'createdAt': createdAt,
            }
            post_info_list.append(post_info)
            doc_ref.set(post_info)

        return post_info_list

