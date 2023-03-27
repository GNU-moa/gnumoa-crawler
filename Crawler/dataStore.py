import time
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
            'links' : info[4]
        }

        print(doc_name)
        print(info[2])
        doc_post.set(makeKey)

def Run(departments):
    start_time = time.time()

    for department in departments:
        print(department)
        categoryNames, baseUrls = department.getBaseUrls()
        for baseUrl, categoryName in zip(baseUrls, categoryNames):
            try:
                print(categoryName)
                text, getPostUrls = department.get_posts(baseUrl)
                savePostInfo(department, categoryName, department.get_title_and_context(categoryName, text, getPostUrls))
            except Exception as e:
                print(f"Failed to crawl {department} - {categoryName}: {e}")

    print("--- 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))





