from Crawler.config import *

import time

start_time = time.time()

ls.getUrls()
physics.getUrls()
math.getUrls()

print("--- 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))