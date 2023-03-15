from Crawler.cns import *

import time

start_time = time.time()

ls.start_crawl()
physics.start_crawl()
math.start_crawl()

print("--- 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))