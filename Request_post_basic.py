import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

url = "https://kind.krx.co.kr/disclosure/todaydisclosure.do" # heeader의 request URL을 입력

payload = {
    'method':'searchTodayDisclosureSub',
    'currentPageSize':'15',
    'pageIndex':'1',
    'orderMode':'0',
    'orderStat':'D',
    'forward':'todaydisclosure_sub',
    'chose':'S',
    'todayFlag':'Y',
    'selDate':'2025-08-01' # 날짜를 변경할 수 있음
} # payload부분의 값이 있는 부분 딕셔너리 형태로 입력

data = rq.post(url, payload) # post 방식
data

html = BeautifulSoup(data.content)
html # 엑셀데이터가 html형태로 변경되어 복잡하게 보임 -> 데이터프레임 형태로 변형 필요

html_unicode = html.prettify() # prettify()sms html을 유니코드 형태로 돌려줌
html_unicode
tbl = pd.read_html(html_unicode) # 테이블 형태의 데이터기 때문에 pandas read_html()을 이용 손쉽게 불러올 수 있음
