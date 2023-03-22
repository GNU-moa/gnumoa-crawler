from .firebase import db
def ChkLastNum():
    docs = db.collection('lastNoticeNum').stream()
    doc_names = [doc.id for doc in docs]
    lastNums = []
    for doc_name in doc_names:
        doc_ref = db.collection('lastNoticeNum').document(doc_name)
        doc = doc_ref.get()
        data = doc.to_dict()
        lastNums.append(data.get('LastNum'))

    print(doc_names)
    print(lastNums)
    return doc_names, lastNums

