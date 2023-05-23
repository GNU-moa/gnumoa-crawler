#수의과대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "수의과대학"

vet = Crawler(
    departmentCollege,
    departmentName_ko = "수의과대학",
    departmentName_en = "vet",
    categoryTags = [["공지사항", 2134, 1184], ["취업정보",2137,1187]]
)

arrvet = [vet]