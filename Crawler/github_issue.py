from github import Github
import os
from dotenv import load_dotenv
load_dotenv()

def github_issue(department, err):
    # 깃허브 이슈에 글을 등록하는 함수
    # department: 학과 이름(ko)
    # err: 에러 메시지
    title = f'[{department}] {err}'
    print(title)
    GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
    GITHUB_REPOSITORY = os.environ['GITHUB_REPOSITORY']
    repo = Github(GITHUB_TOKEN).get_repo(GITHUB_REPOSITORY)
    #repo.create_issue(title=title, body=err)
