import time
from .cns import arrcns
from .getUrlHtml import *
from .firebase import db

def savePostInfo(department,categoryName, AllInfo):
    for info in AllInfo:
        doc_name = department.departmentName_en + '_' + categoryName+'_'+ info[1]
        doc_post = db.collection(department.departmentName_en).document(doc_name)
        makeKey = {
            'Cur_Notice_Url' : info[0],
            'title' : info[2],
            'context' : info[3],
            'categoryName' : categoryName,
        }

        print(doc_name)
        print(info[2])
        doc_post.set(makeKey)

def Run():
    start_time = time.time()

    for department in arrcns:
        i = 0
        categoryNames, baseUrls = department.getBaseUrls()
        for baseUrl in baseUrls:
            text, getPostUrls = get_posts(baseUrl)
            savePostInfo(department,categoryNames[i], get_title_and_context(department,categoryNames[i] ,text, getPostUrls))
            i += 1

    print("--- 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))





