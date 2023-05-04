#경영대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "biz"

business = Crawler(
    departmentCollege,
    departmentName_ko = "경영학부",
    departmentName_en = "business",
    categoryTags = [["공지사항", 6632, 2340], ["취업정보",6626,2338]]
)

trade = Crawler(
    departmentCollege,
    departmentName_ko = "국제통상학부",
    departmentName_en = "trade",
    categoryTags = [["공지사항-가좌", 5679, 2077],["공지사항-칠암", 5680, 2078], ["취업정보",5686,2082]]
)

accounting = Crawler(
    departmentCollege,
    departmentName_ko = "회계세무학부",
    departmentName_en = "accounting",
    categoryTags = [["공지사항-회계세무학부", 6067, 2172],["공지사항-회계학과(구경상대)", 6068, 2173], ["공지사항-회계학과(구경남과기대)", 6069, 2174]]
)

mis = Crawler(
    departmentCollege,
    departmentName_ko = "경영정보학과",
    departmentName_en = "mis",
    categoryTags = [["공지사항", 3208, 1441], ["취업정보",3217,1447], ["채용공고",7693,2606]]
)

industry = Crawler(
    departmentCollege,
    departmentName_ko = "산업경영학과",
    departmentName_en = "industry",
    categoryTags = [["공지사항", 6231, 2222]]
)

smart = Crawler(
    departmentCollege,
    departmentName_ko = "스마트유통물류학과",
    departmentName_en = "smart",
    categoryTags = [["공지사항", 6003, 2157], ["취업정보",6001,2156]]
)


arrbiz = [business, trade, accounting, mis, industry, smart]
