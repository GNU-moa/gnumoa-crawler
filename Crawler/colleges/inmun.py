# 인문대학 config 파일
from ..crawler import Crawler

departmentCollege = "inmun"

engLiter = Crawler(
    departmentCollege,
    departmentName_ko = "영어영문학부 영어영문학전공",
    departmentName_en = "english",
    categoryTags = [["공지사항", 6166, 2206], ["채용정보",6182,  2215]]
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
    categoryTags = [["학사", 7699, 2609], ["장학-등록", 7698, 2608], ["행사-기타", 7700, 2610], ["외국인 유학생 안내", 7701, 2611]]
)

#공지를 왜 이렇게 세분화 해둔거지,,? 이렇게 되면 몇년 전 공지들도 들고와짐
german = Crawler(
    departmentCollege,
    departmentName_ko = "독어독문학과",
    departmentName_en = "dokmun",
    categoryTags = [["졸업", 3972, 1648], ["학사", 7710, 2615], ["장학", 3973, 1649], ["수업", 3974, 1650],["교환학생 및 해외수학", 3975, 1651],["행사", 3976, 1652],["기타", 3977, 1653]]
)

russia = Crawler(
    departmentCollege,
    departmentName_ko = "러시아학과",
    departmentName_en = "russia",
    categoryTags = [["공지사항", 3286, 1463]]
)

#학과에서 공지사항을 안함,,?
minsok = Crawler(
    departmentCollege,
    departmentName_ko = "민속무용학과",
    departmentName_en = "minsok",
    categoryTags = [["학사정보", 3286, 1463], ["자료실", 3864, 1630]]
)

france = Crawler(
    departmentCollege,
    departmentName_ko = "불어불문학과",
    departmentName_en = "france",
    categoryTags = [["학부", 2794, 1305], ["장학금-장학생", 2795, 1306], ["기관공지사항", 2796, 1307]]
)

history = Crawler(
    departmentCollege,
    departmentName_ko = "사학과",
    departmentName_en = "his",
    categoryTags = [["공지사항", 6780, 1348], ["장학정보", 6781, 2367], ["취업정보", 6782, 1351]]
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
    categoryTags = [["공지사항", 3257, 1458]]
)

hanmun = Crawler(
    departmentCollege,
    departmentName_ko = "한문학과",
    departmentName_en = "hanmun",
    categoryTags = [["학사", 10507, 3291], ["장학-등록", 3362, 1503], ["진로-취업", 3357, 1498], ["행사-기타", 12295, 3779],["비교과프로그램", 13210, 4059]]
)

#arrinmun = [german, hanmun]
arrinmun = [engLiter, engLang, korea, german, russia, minsok, france, history, china, sophia, hanmun]
