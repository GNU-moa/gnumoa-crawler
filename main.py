import time
from Crawler.cns import arrcns
from Crawler.getUrlHtml import *
from Crawler.dataStore import *

start_time = time.time()
""" 10개 초기화
for department in arrcns:
    i = 0
    categoryNames, baseUrls = department.getBaseUrls()
    for baseUrl in baseUrls:
        text, getPostUrls = get_posts(baseUrl)
        savePostInfo(categoryNames[i],department, get_title_and_context(text, getPostUrls))
"""


doc_names, lastNums = ChkLastNum()
chkIndex = 0

for department in arrcns:
    i=0
    categoryNames, baseUrls = department.getBaseUrls()
    for baseUrl in baseUrls:
        text, getPostUrls = get_posts(baseUrl)
        print(lastNums[chkIndex], text)
        if lastNums[chkIndex] != text:
            num = str(int(text) - int(lastNums[chkIndex]))
            print(doc_names[chkIndex] + " " + num + "개")
        else:
            print(doc_names[chkIndex] + " 변경사항 없음")
        saveLastNum(department, categoryNames[i], text)
        i += 1
        chkIndex += 1

print("--- 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))