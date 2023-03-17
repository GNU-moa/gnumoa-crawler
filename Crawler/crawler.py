import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self,
                 departmentName_ko,
                 departmentName_en,
                 categoryTags):
        self.departmentName_ko = departmentName_ko
        self.departmentName_en = departmentName_en
        self.categoryTags = categoryTags
    
    def start_crawl(self): #10개 공지들 url 반환
        baseUrls = self.getBaseUrls()
        for baseUrl in baseUrls:
            parsed_html = self.do_html_crawl(baseUrl)
            return self.get_posts(parsed_html, baseUrl)
        
    def getBaseUrls(self): #공지사항 url 반환
        baseUrls = []
        for categoryTag in self.categoryTags:
            categoryName = categoryTag[0]
            mi = categoryTag[1]
            bbsId = categoryTag[2]
            baseUrl = f'https://www.gnu.ac.kr/{self.departmentName_en}/na/ntt/selectNttList.do?mi={mi}&bbsId={bbsId}'
            baseUrls.append(baseUrl)
        return baseUrls
    
    def do_html_crawl(self, baseUrl):
        request = requests.get(baseUrl)
        parsed_html = BeautifulSoup(request.text, 'html.parser')
        return parsed_html

    def get_posts(self, parsed_html, baseUrl):
        getNums = parsed_html.find_all('td', {'class': 'BD_tm_none'})
        CountIndex = 0 #필독 공지 걸러내기
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
        for i in range(CountIndex, CountIndex+10):
            postUrl = f'{baseUrl.replace("selectNttList", "selectNttInfo")}&nttSn={GetDataIds[i]}'
            getPostUrls.append(postUrl)

        return text, getPostUrls

    def get_title_and_context(self):
        text, Urls = self.start_crawl()

        all_ten_info = []
        for i in range(10):
            #allText[0] = 공지 url , allText[1] = 공지 번호 , allText[2] = 공지 제목 , allText[3] = 공지 내용
            allText = []
            url = Urls[i]

            allText.append(url)
            allText.append(str(int(text) - 9 + i))

            title = self.do_html_crawl(url).find("th", class_="title").get_text(strip=True)
            allText.append(title)

            for context in self.do_html_crawl(url).find_all('tr', class_='cont'):
                title_text = context.text.strip()
                allText.append(title_text)

            all_ten_info.append(allText)

        return all_ten_info


