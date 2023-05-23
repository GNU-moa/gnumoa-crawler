#약학대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "약학대학"

pharm = Crawler(
    departmentCollege,
    departmentName_ko = "약학대학",
    departmentName_en = "pharm",
    categoryTags = [["공지사항", 1931, 1156]]
)

arrpharm = [pharm]