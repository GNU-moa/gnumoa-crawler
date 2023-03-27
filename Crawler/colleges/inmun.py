# 인문대학 config 파일
from ..crawler import Crawler

korea = Crawler(
    departmentName_ko = "국어국문학과",
    departmentName_en = "korea",
    categoryTags = [["학사", 7699, 2609], ["장학-등록", 7698, 2608], ["행사-기타", 7700, 2610], ["외국인 유학생 안내", 7701, 2611]]
)

arrinmun = [korea]