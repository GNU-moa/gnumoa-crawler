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
    
    def start_crawl(self):
        baseUrls = self.getBaseUrls()
        for baseUrl in baseUrls:
            print(baseUrl)
            parsed_html = self.do_html_crawl(baseUrl)
            self.get_posts(parsed_html, baseUrl)
        
        
    def getBaseUrls(self):
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

        for i in range(CountIndex, CountIndex+10):
            postUrl = f'{baseUrl.replace("selectNttList", "selectNttInfo")}&nttSn={GetDataIds[i]}'
            print(postUrl)
