import requests as rq
from bs4 import BeautifulSoup

url = "https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258"
data = rq.get(url)
html = BeautifulSoup(data.content)
html

html_title = html.select('dl > dd.articleSubject > a') 
html_title[0]['title'] # 속성 이름을 이용
html_title[0].text # text 추출 -> 속성값에도 기사제목이 있고, text로도 있어 둘다 이용 가능

[i['title'] for i in html_title]
[i.text for i in html_title]
