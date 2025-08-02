import requests as rq

url = "https://quotes.toscrape.com/"
quote = rq.get(url)
quote.content # 텍스트 형식

from bs4 import BeautifulSoup

quote_html = BeautifulSoup(quote.content) # BS로 객체 변환
quote_html

# find_all 함수 사용법
quote_div = quote_html.find_all('div', class_='quote') # div 태그들 전부 가저오기
quote_div
quote_div[0].find_all('span', class_='text')[0].text # 첫번째 div 태그에서 글자 부분만 추출하는 법

[i.find_all('span', class_='text')[0].text for i in quote_div] # 리스트 내포형으로 반복하여 추출

# select 함수 사용법
quote_text = quote_html.select('div.quote > span.text')
quote_text
quote_text[0].text # 첫번째 명언 텍스트 추출 방법

[i.text for i in quote_text] # 리스트 내포형으로 반복하여 추출

# 추가 예제
# 1) 명언을 말한 사람 추출
quote_author = quote_html.select('div.quote > span > small.author')
quote_author[0].text 

[i.text for i in quote_author] # 리스트 내포문을 이용 추출

# 2) about(링크)에 대한 추출 -> herf 속성값이 존재
author_link = quote_html.select('div.quote > span > a')
author_link[0]['href'] # 속성값은 추출하는 방법은 속성 이름을 입력

[i['href'] for i in author_link] # 리스트 내포문을 이용 추출







