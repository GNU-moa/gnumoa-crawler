import time
from Crawler.cns import arrcns
from Crawler.getUrlHtml import *

start_time = time.time()

for departement in arrcns:
    for baseUrl in departement.getBaseUrls():
        text, getPostUrls = get_posts(baseUrl)
        saveInfo(departement, get_title_and_context(text, getPostUrls))


print("--- 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))