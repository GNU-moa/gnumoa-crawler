from Crawler.cns import *

import time

start_time = time.time()
print('생명과학')
ls.start_crawl()

print('물리학과')
physics.start_crawl()

print('수학과')
math.start_crawl()

print("--- 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))