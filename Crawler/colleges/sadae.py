# 본부대학2 config 파일 완료
from ..crawler import Crawler

departmentCollege = "sadae"

pedagogy = Crawler(
    departmentCollege,
    departmentName_ko = "교육학과",
    departmentName_en = "pedagogy",
    categoryTags = [["공지사항", 4609, 1830], ["취업정보",4636,1851]]
)

korlan = Crawler(
    departmentCollege,
    departmentName_ko = "국어교육과",
    departmentName_en = "korlan",
    categoryTags = [["공지사항", 6347, 2261], ["취업정보",6370,2273]]
)

history = Crawler(
    departmentCollege,
    departmentName_ko = "역사교육과",
    departmentName_en = "history",
    categoryTags = [["공지사항", 4265, 1708], ["취업정보",6657,2348]]
)

englishedu = Crawler(
    departmentCollege,
    departmentName_ko = "영어교육과",
    departmentName_en = "englishedu",
    categoryTags = [["공지사항", 4329, 1738]]
)

ecedu = Crawler(
    departmentCollege,
    departmentName_ko = "유아교육과",
    departmentName_en = "ecedu",
    categoryTags = [["공지사항", 2820, 1316]]
)

ethics = Crawler(
    departmentCollege,
    departmentName_ko = "윤리교육과",
    departmentName_en = "ethics",
    categoryTags = [["공지사항", 10938, 3381]]
)

sed = Crawler(
    departmentCollege,
    departmentName_ko = "일반사회교육과",
    departmentName_en = "sed",
    categoryTags = [["공지사항", 3709, 1595]]
)

edjapan = Crawler(
    departmentCollege,
    departmentName_ko = "일어교육과",
    departmentName_en = "edjapan",
    categoryTags = [["공지사항", 4889, 1928]]
)

geoedu = Crawler(
    departmentCollege,
    departmentName_ko = "지리교육과",
    departmentName_en = "geoedu",
    categoryTags = [["공지사항", 4415, 1782]]
)

physed = Crawler(
    departmentCollege,
    departmentName_ko = "물리교육과",
    departmentName_en = "physed",
    categoryTags = [["공지사항", 3671, 1583]]
)

bioedu = Crawler(
    departmentCollege,
    departmentName_ko = "생물교육과",
    departmentName_en = "bioedu",
    categoryTags = [["공지사항", 4398, 1773], ["취업-상담",4412,1780]]
)

mathedu = Crawler(
    departmentCollege,
    departmentName_ko = "수학교육과",
    departmentName_en = "mathedu",
    categoryTags = [["공지사항", 3123, 1412]]
)

chemedu = Crawler(
    departmentCollege,
    departmentName_ko = "화학교육과",
    departmentName_en = "chemedu",
    categoryTags = [["공지사항", 4510, 1805]]
)

artedu = Crawler(
    departmentCollege,
    departmentName_ko = "미술교육과",
    departmentName_en = "artedu",
    categoryTags = [["공지사항", 4701,1874]]
)

musicedu = Crawler(
    departmentCollege,
    departmentName_ko = "음악교육과",
    departmentName_en = "musicedu",
    categoryTags = [["공지사항", 4440, 1790]]
)

physicaledu = Crawler(
    departmentCollege,
    departmentName_ko = "체육교육과",
    departmentName_en = "physicaledu",
    categoryTags = [["공지사항",4527, 1812]]
)

arrsadae = [pedagogy, korlan, history, englishedu, ecedu, ethics, sed, edjapan, geoedu, physed, bioedu, mathedu, chemedu, artedu, musicedu, physicaledu]