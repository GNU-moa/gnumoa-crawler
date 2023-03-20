# firebase 관련 설정들을 모아둔 파일입니다.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import json

if os.environ.get("FIREBASE_ADMIN_SDK"): # Github Actions에서 실행될 때
    cred = credentials.Certificate(json.loads(os.environ.get("FIREBASE_ADMIN_SDK")))
    print(cred)
else: # 로컬에서 실행될 때
  cred = credentials.Certificate(os.getcwd() + "/gnu-moa-firebase-adminsdk.json")

firebase_admin.initialize_app(cred)

db = firestore.client()
