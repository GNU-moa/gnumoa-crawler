#의과대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "의과대학"

medicine = Crawler(
    departmentCollege,
    departmentName_ko = "의과대학",
    departmentName_en = "medicine",
    categoryTags = [["공지사항", 1716, 1119]]
)

arrmedicine = [medicine]