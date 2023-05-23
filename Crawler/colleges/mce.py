# 본부대학1 config 파일 완료
from ..crawler import Crawler

departmentCollege = "본부대학1"

mce = Crawler(
    departmentCollege,
    departmentName_ko = "기계융합공학과",
    departmentName_en = "mce",
    categoryTags = [["공지사항", 4782, 1889], ["취업정보",12199,3759]]
)

arrmce = [mce]