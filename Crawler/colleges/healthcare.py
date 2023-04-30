# 본부대학2 config 파일 완료
from ..crawler import Crawler

departmentCollege = "healthcare"

healthcare = Crawler(
    departmentCollege,
    departmentName_ko = "휴먼헬스케어학과",
    departmentName_en = "healthcare",
    categoryTags = [["공지사항", 6033, 2166], ["취업정보",6028,2161]]
)

arrhealthcare = [healthcare]