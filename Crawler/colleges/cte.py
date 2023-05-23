#융합기술공과대학 config 파일 완료
from ..crawler import Crawler

departmentCollege = "융합기술공과대학"

mm = Crawler(
    departmentCollege,
    departmentName_ko = "기계소재융합공학부",
    departmentName_en = "mm",
    categoryTags = [["공지사항", 6846, 2199], ["취업정보",6847,2196]]
)

mecha = Crawler(
    departmentCollege,
    departmentName_ko = "메카트로닉스공학부",
    departmentName_en = "mecha",
    categoryTags = [["학부공지", 2853, 1331], ["졸업공지",8293,2759], ["장학공지",2854,1332], ["취업정보",2850,1329]]
)

cele = Crawler(
    departmentCollege,
    departmentName_ko = "융합전자공학부",
    departmentName_en = "cele",
    categoryTags = [["학부공지", 4664, 1858], ["장학공지",4665,1859], ["취업정보",4666,1860]]
)

energyeng = Crawler(
    departmentCollege,
    departmentName_ko = "에너지공학과",
    departmentName_en = "energyeng",
    categoryTags = [["공지사항", 5895, 2142]]
)

car = Crawler(
    departmentCollege,
    departmentName_ko = "미래자동차공학과",
    departmentName_en = "car",
    categoryTags = [["공지사항", 5865, 2131], ["취업정보",5862,2128]]
)

arrcte = [mm, mecha, cele, energyeng, car]