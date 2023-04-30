#건설환경공과대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "cee"

civilinfra = Crawler(
    departmentCollege,
    departmentName_ko = "건설시스템공학과",
    departmentName_en = "civilinfra",
    categoryTags = [["공지사항", 6653, 2344], ["취업정보",6648,2341]]
)

im = Crawler(
    departmentCollege,
    departmentName_ko = "인테리어재료공학과",
    departmentName_en = "im",
    categoryTags = [["공지사항", 4620, 1840]]
)

landscape = Crawler(
    departmentCollege,
    departmentName_ko = "조경학과",
    departmentName_en = "landscape",
    categoryTags = [["공지사항", 6474, 2303], ["취업정보",6495,2313]]
)

env = Crawler(
    departmentCollege,
    departmentName_ko = "환경공학과",
    departmentName_en = "env",
    categoryTags = [["공지사항", 6394, 2281], ["취업정보",6390,2277]]
)

design = Crawler(
    departmentCollege,
    departmentName_ko = "디자인비즈니스학과",
    departmentName_en = "design",
    categoryTags = [["공지사항", 5257, 1993]]
)

arrcee = [civilinfra, im, landscape, env, design]