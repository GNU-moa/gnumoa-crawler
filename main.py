from Crawler.dataStore import Run
from Crawler import *
import time

start_time = time.time()
Run(arrcns) # 자연과학대학
Run(arrinmun) # 인문대학
print(f"--- 전체 학과 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))


