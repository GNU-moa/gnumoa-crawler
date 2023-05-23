#간호대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "간호대학"

cap = Crawler(
    departmentCollege,
    departmentName_ko = "간호대학",
    departmentName_en = "cap",
    categoryTags = [["공지사항", 1614, 1103], ["취업정보",1634,1110]]
)

arrcap = [cap]