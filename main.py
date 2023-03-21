import time
from Crawler.cns import arrcns
from Crawler.getUrlHtml import *
from Crawler.dataStore import *
start_time = time.time()
"""
for department in arrcns:
    i = 0
    categoryNames, baseUrls = department.getBaseUrls()
    for baseUrl in baseUrls:
        text, getPostUrls = get_posts(baseUrl)
        saveLastNum(department, categoryNames[i], text)
        savePostInfo(categoryNames[i],department, get_title_and_context(text, getPostUrls))
        i += 1
"""

print("--- 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))