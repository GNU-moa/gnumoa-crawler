from Crawler.dataStore import Run
from Crawler import *
import time

start_time = time.time()
#Run(arrinmun) # 인문대학
#Run(arrcss) # 사회과학대학
#Run(arrcns) # 자연과학대학
#Run(arrbiz) # 경영대학
#Run(arrce) # 공과대학
#Run(arrcals) # 농업생명과학대학
#Run(arrlaw) # 법과대학
#Run(arrsadae) # 사범대학
#Run(arrvet) # 수의과대학
#Run(arrmedicine) # 의과대학
#Run(arrcap) # 간호대학
Run(arrmarsci) # 해양과학대학
#Run(arrpharm) # 약학대학
#Run(arrmce) # 본부대학1
#Run(arrcee) # 건설환경공과대학
#Run(arrcte) # 융합기술공과대학
#Run(arrhealthcare) # 본부대학2


print(f"--- 전체 학과 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))


