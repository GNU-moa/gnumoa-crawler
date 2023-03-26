import requests
from bs4 import BeautifulSoup
from .firebase import db

def do_html_crawl(Url):
    request = requests.get(Url)
    parsed_html = BeautifulSoup(request.text, 'html.parser')
    return parsed_html
def get_posts(baseUrl):
    parsed_html = do_html_crawl(baseUrl)
    getNums = parsed_html.find_all('td', {'class': 'BD_tm_none'})
    CountIndex = 0  # 필독 공지 걸러내기
    for getNum in getNums:
        text = getNum.text.strip()
        if text != '공지':
            break
        CountIndex = CountIndex + 1

    GetDataWords = parsed_html.find_all('a', {'class': 'nttInfoBtn'})

    GetDataIds = []
    for Word in GetDataWords:
        GetDataIds.append(Word['data-id'])

    getPostUrls = []
    for i in range(CountIndex, CountIndex + 10):
        postUrl = f'{baseUrl.replace("selectNttList", "selectNttInfo")}&nttSn={GetDataIds[i]}'
        getPostUrls.append(postUrl)

    return text, getPostUrls

def get_title_and_context(department, categoryName,text, postUrls):
    all_info = []
    for i in range(10):
        #Url을 html로 변환
        parsed_html = do_html_crawl(postUrls[i])

        chkDoc = department.departmentName_en + '_' + categoryName+'_'+ str(int(text) - 9 + i)
        doc_ref = db.collection(department.departmentName_en).document(chkDoc)
        if doc_ref.get().exists:
            pass
        else:
            # allText[0] = 공지 url , allText[1] = 공지 번호 , allText[2] = 공지 제목 , allText[3] = 공지 내용
            allText = []

            allText.append(postUrls[i])
            allText.append(str(int(text) - 9 + i))

            title = parsed_html.find("th", class_="title").get_text(strip=True)
            allText.append(title)

            for context in parsed_html.find_all('tr', class_='cont'):
                title_text = context.text.strip()
                allText.append(title_text)

            ul_file = parsed_html.find('ul', {'class': 'file'})
            li_tags = ul_file.find_all('li')

            links = []
            for li in li_tags:
                a_tag = li.find('a')
                if a_tag is not None:
                    link = a_tag.get('href')
                    links.append('https://www.gnu.ac.kr'+ link)

            allText.append(links)

            all_info.append(allText)

    return all_info






