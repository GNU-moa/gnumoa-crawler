#농업생명과학대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "농업생명과학대학"


abit = Crawler(
    departmentCollege,
    departmentName_ko = "동물생명융합학부",
    departmentName_en = "abit",
    categoryTags = [["공지사항",6600, 2331], ["취업정보",6605,2335]]
)

foodsci = Crawler(
    departmentCollege,
    departmentName_ko = "식품공학과",
    departmentName_en = "foodsci",
    categoryTags = [["공지사항", 10198, 3190], ["취업정보",5741,2092]]
)

hortic = Crawler(
    departmentCollege,
    departmentName_ko = "원예과학부",
    departmentName_en = "hortic",
    categoryTags = [["공지사항", 7496, 2029], ["취업정보",5482,2035]]
)

ase = Crawler(
    departmentCollege,
    departmentName_ko = "축산과학부",
    departmentName_en = "as",
    categoryTags = [["공지사항", 5519, 2040], ["취업정보",5522,2043]]
)

fr = Crawler(
    departmentCollege,
    departmentName_ko = "환경산림과학부",
    departmentName_en = "fr",
    categoryTags = [["공지사항", 5651, 2071], ["취업정보",5650,2070]]
)

agronomy = Crawler(
    departmentCollege,
    departmentName_ko = "농학과",
    departmentName_en = "agronomy",
    categoryTags = [["공지사항", 7181, 2468]]
)

smartagro = Crawler(
    departmentCollege,
    departmentName_ko = "스마트농산업학과",
    departmentName_en = "smartagro",
    categoryTags = [["공지사항", 4810, 1899]]
)

ab = Crawler(
    departmentCollege,
    departmentName_ko = "식물의학과",
    departmentName_en = "ab",
    categoryTags = [["공지사항", 4116, 1682], ["취업정보",4071,2114]]
)

alc = Crawler(
    departmentCollege,
    departmentName_ko = "환경생명화학과",
    departmentName_en = "alc",
    categoryTags = [["공지사항", 3515, 1557], ["취업정보",3517,1558]]
)

ems = Crawler(
    departmentCollege,
    departmentName_ko = "환경재료과학과",
    departmentName_en = "ems",
    categoryTags = [["공지사항", 7000,2427]]
)

bime = Crawler(
    departmentCollege,
    departmentName_ko = "생물산업기계공학과",
    departmentName_en = "bime",
    categoryTags = [["공지사항", 4228, 1714], ["취업정보",4230,1716]]
)

agrieng = Crawler(
    departmentCollege,
    departmentName_ko = "지역시스템공학과",
    departmentName_en = "agrieng",
    categoryTags = [["공지사항", 5288, 1997], ["취업정보",11777,3632]]
)

arrcals = [abit, foodsci, hortic, ase, fr, agronomy, smartagro, ab, alc, ems, bime, agrieng]