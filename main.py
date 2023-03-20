from Crawler.cns import *
from Crawler.firebase import db
from Crawler.github_issue import github_issue

import time

start_time = time.time()
print('생명과학')
ls.start_crawl()

print('물리학과')
physics.start_crawl()

print('수학과')
math.start_crawl()

print("--- 파싱 진행 시간: %s 초 ---" % (time.time() - start_time))

# firebase 연동 테스트
doc_ref = db.collection(u'science').document(u'RJCkxzXGtk2apM3EBWm8')
doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such document!')