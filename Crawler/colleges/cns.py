# 자연과학대학 config 파일
from ..crawler import Crawler

departmentCollege = "cns"

ls = Crawler(
    departmentCollege,
    departmentName_ko = "생명공학부",
    departmentName_en = "ls",
    categoryTags = [["공지사항", 13180, 4048]]
)

physics = Crawler(
    departmentCollege,
    departmentName_ko = "물리학과",
    departmentName_en = "physics",
    categoryTags = [["학사공지", 3937, 1639], ["장학관련", 3938, 1640], ["취업정보", 3939, 1641]]
)

math = Crawler(
    departmentCollege,
    departmentName_ko = "수학과",
    departmentName_en = "math",
    categoryTags = [["공지사항", 4006, 1666]]
)

foodnutri = Crawler(
    departmentCollege,
    departmentName_ko = "식품영양학과",
    departmentName_en = "foodnutri",
    categoryTags = [["전체공지", 12484, 2439],["공지(~2021학번까지)", 12485, 3788],["공지(2022학번 이후)", 12486, 3789],["취업정보",7070, 2440]]
)

cloth = Crawler(
    departmentCollege,
    departmentName_ko = "의류학과",
    departmentName_en = "cloth",
    categoryTags = [["공지사항", 4325, 1735]]
)

stat = Crawler(
    departmentCollege,
    departmentName_ko = "정보통계학과",
    departmentName_en = "stat",
    categoryTags = [["공지사항", 12107, 3753]]
)

pharmgine = Crawler(
    departmentCollege,
    departmentName_ko = "제약공학과",
    departmentName_en = "pharmgine",
    categoryTags = [["공지사항", 7144, 1886]]
)

geology = Crawler(
    departmentCollege,
    departmentName_ko = "지질과학과",
    departmentName_en = "geology",
    categoryTags = [["공지사항", 2918, 1344]]
)

biomat = Crawler(
    departmentCollege,
    departmentName_ko = "항노화신소재과학과",
    departmentName_en = "biomat",
    categoryTags = [["공지사항", 3071, 1394]]
)

chem = Crawler(
    departmentCollege,
    departmentName_ko = "화학과",
    departmentName_en = "chem",
    categoryTags = [["공지사항", 5144, 1971]]
)

cs = Crawler(
    departmentCollege,
    departmentName_ko = "컴퓨터과학부 컴퓨터과학전공",
    departmentName_en = "cs",
    categoryTags = [["공지사항", 6694, 2351]]
)

cse = Crawler(
    departmentCollege,
    departmentName_ko = "컴퓨터과학부 컴퓨터소프트웨어전공",
    departmentName_en = "cse",
    categoryTags = [["공지사항", 5550, 20048], ["공모전 및 대회",5554,2052]]
)

arrcns = [ls, physics, math, foodnutri, cloth, stat, pharmgine, geology, biomat, chem, cs, cse]