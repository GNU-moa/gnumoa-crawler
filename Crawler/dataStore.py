import time
import traceback
from .firebase import db

def savePostInfo(department, categoryName, AllInfo):
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
        categoryNames, baseUrls = department.getBaseUrls()
        print(categoryNames)
        for baseUrl, categoryName in zip(baseUrls, categoryNames):
            try:
                text, getPostUrls = department.get_posts(baseUrl)
                savePostInfo(department, categoryName, department.get_title_and_context(categoryName, text, getPostUrls))
            except Exception as e:
                print(f"Failed to crawl {department.departmentName_ko} - {categoryName}: {e}")
                tb = e.__traceback__
                tb_info = traceback.extract_tb(tb)
                for line in tb_info:
                    filename, line_no, func_name, source_code = line
                    print(f"{filename}:{line_no} 에서 {e.__class__.__name__} 발생")

        print(f"--- {department.departmentName_ko} 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))





