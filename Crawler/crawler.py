class Crawler:
    def __init__(self,
                 departmentName_ko,
                 departmentName_en,
                 categoryTags):
        self.departmentName_ko = departmentName_ko
        self.departmentName_en = departmentName_en
        self.categoryTags = categoryTags

    def getBaseUrls(self): #공지사항 url 반환
        baseUrls = []
        for categoryTag in self.categoryTags:
            categoryName = categoryTag[0]
            mi = categoryTag[1]
            bbsId = categoryTag[2]
            baseUrl = f'https://www.gnu.ac.kr/{self.departmentName_en}/na/ntt/selectNttList.do?mi={mi}&bbsId={bbsId}'
            baseUrls.append(baseUrl)
        return baseUrls


