#사회과학대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "사회과학대학"

economics = Crawler(
    departmentCollege,
    departmentName_ko = "경제학부",
    departmentName_en = "economics",
    categoryTags = [["공지사항", 6899, 2402], ["취업정보",6904,2406]]
)

socialwelfare = Crawler(
    departmentCollege,
    departmentName_ko = "사회복지학부",
    departmentName_en = "socialwelfare",
    categoryTags = [["공지사항", 6317, 2252], ["취업정보",6313,2249]]
)

socio = Crawler(
    departmentCollege,
    departmentName_ko = "사회학과",
    departmentName_en = "socio",
    categoryTags = [["공지사항", 6330, 2256], ["취업정보",13282,4076],["대외활동",13283,4077]]
)

psychology = Crawler(
    departmentCollege,
    departmentName_ko = "심리학과",
    departmentName_en = "psychology",
    categoryTags = [["공지사항", 5603, 2061], ["취업정보",5606,2064]]
)

cfc = Crawler(
    departmentCollege,
    departmentName_ko="아동가족학과",
    departmentName_en="cfc",
    categoryTags= [["공지사항",4716,1882],["취업정보",4720,1885]]
)

polisci = Crawler(
    departmentCollege,
    departmentName_ko = "정치외교학과",
    departmentName_en = "polisci",
    categoryTags = [["공지사항", 3621, 1569], ["취업정보",3622,1570]]
)


pa = Crawler(
    departmentCollege,
    departmentName_ko = "행정학과",
    departmentName_en = "pa",
    categoryTags = [["공지사항", 5174, 1981], ["대외활동-취업정보",5177,1984]]
)

arrcss = [economics, socialwelfare, socio, psychology,cfc, polisci, pa]