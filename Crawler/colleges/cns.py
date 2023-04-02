# 자연과학대학 config 파일
from ..crawler import Crawler

departmentCollege = "cns"

ls = Crawler(
    departmentCollege,
    departmentName_ko = "생명공학부",
    departmentName_en = "ls",
    categoryTags = [["공지사항", 13180, 4048]]
)

physics = Crawler(
    departmentCollege,
    departmentName_ko = "물리학과",
    departmentName_en = "physics",
    categoryTags = [["학사공지", 3937, 1639], ["장학관련", 3938, 1640], ["취업정보", 3939, 1641]]
)

math = Crawler(
    departmentCollege,
    departmentName_ko = "수학과",
    departmentName_en = "math",
    categoryTags = [["공지사항", 4006, 1666]]
)

arrcns = [ls]