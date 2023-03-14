class Crawler:
    def __init__(self,
                 departmentName_ko,
                 departmentName_en,
                 categoryTags):
        self.departmentName_ko = departmentName_ko
        self.departmentName_en = departmentName_en
        self.categoryTags = categoryTags
        
    def getData(self):
        for categoryTag in self.categoryTags:
            categoryName = categoryTag[0]
            mi = categoryTag[1]
            bbsId = categoryTag[2]
            baseUrl = f'https://www.gnu.ac.kr/{self.departmentName_en}/na/ntt/selectNttList.do?mi={mi}&bbsId={bbsId}'
            print(baseUrl)

ls = Crawler(
    departmentName_ko = "생명공학부",
    departmentName_en = "ls",
    categoryTags = [["공지사항", 13180, 4048], ["장학", 11111, 4444]]
)

ls.getData()