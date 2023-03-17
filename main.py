import time
from Crawler.firebase import db
from Crawler.cns import *

start_time = time.time()


for i in range(10):
    doc_name = ls.departmentName_en + '_' + ls.get_title_and_context()[i][1]
    doc_ref = db.collection(ls.departmentName_en).document(doc_name)

    makeKey = {
        'Cur_Notice_Url' : ls.get_title_and_context()[i][0],
        'title' : ls.get_title_and_context()[i][2],
        'context' : ls.get_title_and_context()[i][3]
    }
    doc_ref.set(makeKey)


print("--- 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))