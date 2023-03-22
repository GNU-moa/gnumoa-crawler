# firebase 관련 설정들을 모아둔 파일입니다.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

cred = credentials.Certificate("C:\gnu-moa-firebase-adminsdk-93zd8-8e1fb6f582.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
