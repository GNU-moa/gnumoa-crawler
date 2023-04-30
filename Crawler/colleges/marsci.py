#해양과학대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "marsci"

fba = Crawler(
    departmentCollege,
    departmentName_ko = "해양수산경영학과",
    departmentName_en = "fba",
    categoryTags = [["공지사항", 3450, 1541]]
)

mirae = Crawler(
    departmentCollege,
    departmentName_ko = "미래산업융합학과",
    departmentName_en = "mirae",
    categoryTags = [["공지사항", 4861, 1915]]
)

sea = Crawler(
    departmentCollege,
    departmentName_ko = "양식생명과학과",
    departmentName_en = "sea",
    categoryTags = [["공지사항", 3112, 1405]]
)

#maripoli = Crawler(
#    departmentCollege,
#    departmentName_ko = "해양경찰시스템학과",
#    departmentName_en = "maripoli",
#    categoryTags = [["공지사항", 3538, 1561], ["취업-장학",3542,1565]]
#)

gse = Crawler(
    departmentCollege,
    departmentName_ko = "기계시스템공학과",
    departmentName_en = "gse",
    categoryTags = [["공지사항", 3462, 1543], ["취업정보",3485,1548]]
)

smartam = Crawler(
    departmentCollege,
    departmentName_ko = "스마트에너지기계공학과",
    departmentName_en = "smartam",
    categoryTags = [["공지사항", 3057, 1389], ["취업정보",9329,2952]]
)

naoe = Crawler(
    departmentCollege,
    departmentName_ko = "조선해양공학과",
    departmentName_en = "naoe",
    categoryTags = [["공지사항", 3419, 1533], ["취업정보",3416,1532]]
)

ace = Crawler(
    departmentCollege,
    departmentName_ko = "지능형통신공학과",
    departmentName_en = "ace",
    categoryTags = [["공지사항", 3309, 1469], ["취업정보",3310,1470]]
)

seafood = Crawler(
    departmentCollege,
    departmentName_ko = "해양식품공학과",
    departmentName_en = "seafood",
    categoryTags = [["공지사항", 4486, 1797], ["취업정보",7897,1798]]
)

oce = Crawler(
    departmentCollege,
    departmentName_ko = "해양토목공학과",
    departmentName_en = "oce",
    categoryTags = [["공지사항", 3239, 1454]]
)

marenv = Crawler(
    departmentCollege,
    departmentName_ko = "해양환경공학과",
    departmentName_en = "marenv",
    categoryTags = [["공지사항", 4546, 1818], ["취업정보",4554,1820]]
)

arrmarsci = [fba, mirae, sea, maripoli, gse, smartam, naoe, ace, seafood, oce, marenv]