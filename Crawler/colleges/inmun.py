# 인문대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "inmun"

engLiter = Crawler(
    departmentCollege,
    departmentName_ko = "영어영문학부 영어영문학전공",
    departmentName_en = "english",
    categoryTags = [["공지사항", 6166, 2206], ["취업정보",6182,  2215]]
)

engLang = Crawler(
    departmentCollege,
    departmentName_ko = "영어영문학과 영어전공",
    departmentName_en = "e_language",
    categoryTags = [["공지사항", 6201, 2219]]
)

korea = Crawler(
    departmentCollege,
    departmentName_ko = "국어국문학과",
    departmentName_en = "korea",
    categoryTags = [["학부공지", 7699, 2609], ["장학공지", 7698, 2608], ["행사-기타공지", 7700, 2610]]
)

dokmun = Crawler(
    departmentCollege,
    departmentName_ko = "독어독문학과",
    departmentName_en = "dokmun",
    categoryTags = [["졸업공지", 3972, 1648], ["학부공지", 7710, 2615], ["장학공지", 3973, 1649]]
)

russia = Crawler(
    departmentCollege,
    departmentName_ko = "러시아학과",
    departmentName_en = "russia",
    categoryTags = [["공지사항", 3286, 1463],["취업정보",3287,1464]]
)

#minsok = Crawler(
#    departmentCollege,
#    departmentName_ko = "민속무용학과",
#    departmentName_en = "minsok",
#    categoryTags = [["공지사항", 3286, 1463]]
#)

france = Crawler(
    departmentCollege,
    departmentName_ko = "불어불문학과",
    departmentName_en = "france",
    categoryTags = [["공지사항", 2794, 1305], ["장학공지", 2795, 1306], ["기관공지사항", 2796, 1307]]
)

history = Crawler(
    departmentCollege,
    departmentName_ko = "사학과",
    departmentName_en = "his",
    categoryTags = [["공지사항", 6780, 1348], ["장학공지", 6781, 2367], ["취업정보", 6782, 1351]]
)

china = Crawler(
    departmentCollege,
    departmentName_ko = "중어중문학과",
    departmentName_en = "china",
    categoryTags = [["공지사항", 5436, 2019], ["취업정보", 5444, 2025]]
)

sophia = Crawler(
    departmentCollege,
    departmentName_ko = "철학과",
    departmentName_en = "sophia",
    categoryTags = [["공지사항", 10518, 1458],["취업정보",13320,4089]]
)

hanmun = Crawler(
    departmentCollege,
    departmentName_ko = "한문학과",
    departmentName_en = "hanmun",
    categoryTags = [["학사공지", 10507, 3291], ["장학공지", 3362, 1503], ["취업공지", 3357, 1498], ["행사공지", 12295, 3779],["비교과프로그램", 13210, 4059]]
)

arrinmun = [engLiter, engLang, korea, dokmun, russia, france, history, china, sophia, hanmun]
