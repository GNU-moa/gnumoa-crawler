#법과대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "법과대학"

law = Crawler(
    departmentCollege,
    departmentName_ko = "법과대학",
    departmentName_en = "law",
    categoryTags = [["공지사항", 2644, 1275]]
)

arrlaw = [law]