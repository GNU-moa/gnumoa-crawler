import time
from .cns import arrcns
from .getUrlHtml import *
from .firebase import db

def Run():
    start_time = time.time()

    updates = []

    for department in arrcns:
        i = 0
        categoryNames, baseUrls = department.getBaseUrls()
        for baseUrl in baseUrls:
            updateInfo = []
            collection_ref = len(db.collection(department.departmentName_en).where('categoryName', '==', categoryNames[i]).get())
            text, getPostUrls = get_posts(baseUrl)
            savePostInfo(categoryNames[i],department, get_title_and_context(text, getPostUrls))
            collection_ref2 = len(db.collection(department.departmentName_en).where('categoryName', '==', categoryNames[i]).get())
            updateInfo.append(department.departmentName_en)
            updateInfo.append(categoryNames[i])
            updateInfo.append(collection_ref2-collection_ref)
            i += 1
            updates.append(updateInfo)

    print(updates)

    print("--- 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))





