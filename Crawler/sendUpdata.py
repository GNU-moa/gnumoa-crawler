import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
import os

# Firebase Admin SDK 초기화
if not firebase_admin._apps:
    cred = credentials.Certificate(os.getcwd() + "/gnu-moa-firebase-adminsdk.json")
    firebase_admin.initialize_app(cred)

# 클라우드 메시지 보내기
def send_push_notification(token, majorName, categoryName, title):
    message = messaging.Message(
        token=token,
        notification=messaging.Notification(
            title=majorName + " " + categoryName,
            body=title
        )
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)
