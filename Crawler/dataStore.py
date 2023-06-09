import time
import traceback

def Run(departments):
    start_time = time.time()

    for department in departments:
        categoryNames, baseUrls = department.getBaseUrls()
        for baseUrl, categoryName in zip(baseUrls, categoryNames):
            try:
                CountIndex, GetDataIds, text = department.division_postInfo(baseUrl)
                get_essentialUrls, get_postUrls = department.get_posts(CountIndex, baseUrl, GetDataIds)
                get_essentialUrls.reverse()
                get_postUrls.reverse() # 게시물을 최신순으로 정렬
                department.save_essential_Info(categoryName, GetDataIds, get_essentialUrls)
                department.save_basic_Info(categoryName, text, get_postUrls)
            except Exception as e:
                print(f"Failed to crawl {department.departmentName_ko} - {categoryName}: {e}")
                tb = e.__traceback__
                tb_info = traceback.extract_tb(tb)
                for line in tb_info:
                    filename, line_no, func_name, source_code = line
                    print(f"{filename}:{line_no} 에서 {e.__class__.__name__} 발생")

        print(f"--- {department.departmentName_ko} 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))





