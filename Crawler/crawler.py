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
        
    def getUrls(self):
        for categoryTag in self.categoryTags:
            categoryName = categoryTag[0]
            mi = categoryTag[1]
            bbsId = categoryTag[2]
            baseUrl = f'https://www.gnu.ac.kr/{self.departmentName_en}/na/ntt/selectNttList.do?mi={mi}&bbsId={bbsId}'
            print(self.do_html_crawl(baseUrl))
    
    def do_html_crawl(self, baseUrl):
        request = requests.get(baseUrl)
        parsed_html = BeautifulSoup(request.text, 'html.parser')
        return parsed_html