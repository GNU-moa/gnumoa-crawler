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
            parsed_html = self.do_html_crawl(baseUrl)
        
        
    def getBaseUrls(self):
        baseUrls = [];
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

    def get_posts(self, parsed_html):
        parsed_posts = parsed_html.select('#sub_content > div.subCntBody.clearfix > div.BD_list > table > tbody')