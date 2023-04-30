from Crawler.dataStore import Run
from multiprocessing import Process
from Crawler import *
import time

if __name__ == '__main__':
    start_time = time.time()
    
    p1 = Process(target=Run, args=(arrinmun,))
    p2 = Process(target=Run, args=(arrcss,))
    p3 = Process(target=Run, args=(arrcns,))
    p4 = Process(target=Run, args=(arrbiz,))
    p5 = Process(target=Run, args=(arrce,))
    p6 = Process(target=Run, args=(arrcals,))
    p7 = Process(target=Run, args=(arrlaw,))
    p8 = Process(target=Run, args=(arrsadae,))
    p9 = Process(target=Run, args=(arrvet,))
    p10 = Process(target=Run, args=(arrmedicine,))
    p11 = Process(target=Run, args=(arrcap,))
    p12 = Process(target=Run, args=(arrmarsci,))
    p13 = Process(target=Run, args=(arrpharm,))
    p14 = Process(target=Run, args=(arrmce,))
    p15 = Process(target=Run, args=(arrcee,))
    p16 = Process(target=Run, args=(arrcte,))
    p17 = Process(target=Run, args=(arrhealthcare,))
    
    processes = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"--- 전체 학과 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))




