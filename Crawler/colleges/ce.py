#공과대학 config 파일 완료
#홈페이지 이상 세라믹공학전공, 전자공학과
from ..crawler import Crawler

departmentCollege = "ce"

archeng = Crawler(
    departmentCollege,
    departmentName_ko = "건축공학부",
    departmentName_en = "archeng",
    categoryTags = [["공지사항", 6804, 2378], ["취업정보",6807,2381]]
)

me = Crawler(
    departmentCollege,
    departmentName_ko = "기계공학부",
    departmentName_en = "me",
    categoryTags = [["공지사항", 6418, 2201], ["취업정보",6151,2204]]
)

polymer = Crawler(
    departmentCollege,
    departmentName_ko = "고분자공학전공",
    departmentName_en = "polymer",
    categoryTags = [["공지사항", 10337, 3229], ["취업정보",7667,1677]]
)

metals = Crawler(
    departmentCollege,
    departmentName_ko = "금속재료공학전공",
    departmentName_en = "metals",
    categoryTags = [["공지사항", 3565, 1357], ["취업정보",3610,1358]]
)

ise = Crawler(
    departmentCollege,
    departmentName_ko = "산업시스템공학부",
    departmentName_en = "ise",
    categoryTags = [["공지사항", 2998, 1368], ["장학공지",3003,1374],["취업정보",3006,1376]]
)

anse = Crawler(
    departmentCollege,
    departmentName_ko = "항공우주및소프트웨어공학부",
    departmentName_en = "anse",
    categoryTags = [["공지사항", 3041, 1383], ["취업정보",3052,1387]]
)

arch = Crawler(
    departmentCollege,
    departmentName_ko = "건축학과",
    departmentName_en = "arch",
    categoryTags = [["공지사항", 5709, 2083], ["취업정보",5711,2085]]
)

urban = Crawler(
    departmentCollege,
    departmentName_ko = "도시공학과",
    departmentName_en = "urban",
    categoryTags = [["공지사항", 3094, 1397], ["취업-교육-공모전",3101,1400]]
)

se = Crawler(
    departmentCollege,
    departmentName_ko = "반도체공학과",
    departmentName_en = "se",
    categoryTags = [["공지사항", 5837,2116], ["취업정보",5840,2119]]
)

el = Crawler(
    departmentCollege,
    departmentName_ko = "전기공학과",
    departmentName_en = "el",
    categoryTags = [["공지사항", 3649, 1574], ["취업정보",3652,1576]]
)


control = Crawler(
    departmentCollege,
    departmentName_ko = "제어로봇공학과",
    departmentName_en = "control",
    categoryTags = [["공지사항", 5926, 2147], ["취업정보",5928,2149]]
)

civil = Crawler(
    departmentCollege,
    departmentName_ko = "토목공학과",
    departmentName_en = "civil",
    categoryTags = [["공지사항", 6423, 2289], ["취업정보",6433,2299]]
)

chemeng = Crawler(
    departmentCollege,
    departmentName_ko = "화학공학과",
    departmentName_en = "chemeng",
    categoryTags = [["공지사항", 3894, 1636]]
)

arrce = [archeng, me, polymer, metals, ise, anse, arch, urban, se, el, control, civil, chemeng]