import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_stock_market_capitalization"

tbl = pd.read_html(url)
tbl[0]
tbl[1]


# 테이블 형태의 데이터는 pandas의 read_html함수 사용 시, 매우 손쉽게 불러올 수 있음!!