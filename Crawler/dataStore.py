import time
import traceback

def Run(departments):
    start_time = time.time()

    for department in departments:
        categoryNames, baseUrls = department.getBaseUrls()
        for baseUrl, categoryName in zip(baseUrls, categoryNames):
            try:
                text, getPostUrls = department.get_posts(baseUrl)
                department.get_title_and_context(categoryName, text, getPostUrls)
            except Exception as e:
                print(f"Failed to crawl {department.departmentName_ko} - {categoryName}: {e}")
                tb = e.__traceback__
                tb_info = traceback.extract_tb(tb)
                for line in tb_info:
                    filename, line_no, func_name, source_code = line
                    print(f"{filename}:{line_no} 에서 {e.__class__.__name__} 발생")

        print(f"--- {department.departmentName_ko} 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))





