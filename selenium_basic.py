# 기본 세팅
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # 크롬 제어창 열림

# 기본 조작 방법

url = "http://www.naver.com"
driver.get(url)
driver.page_source # 페이지의 html 정보확인

# 뉴스 링크 클릭
driver.find_element(By.LINK_TEXT, value='뉴스').click() # 링크 텍스트로 엘리먼트 찾기
driver.back() # 뒤로가기

# 검색창 단어 입력해서 클릭하기
driver.find_element(By.CLASS_NAME, value='search_input').send_keys('퀀트 투자 포트폴리오 만들기') # 검색창을 찾아서, 검색어 입력
driver.find_element(By.CLASS_NAME, value='btn_search').send_keys(Keys.ENTER) # 서치 버튼을 찾아서 엔터

# 기존 내용을 지우고 다시 검색
driver.find_element(By.CLASS_NAME, value='box_window').clear() # 검색창에 기존 단어 지우기
driver.find_element(By.CLASS_NAME, value='box_window').send_keys('이현열 퀀트') # 새검색어 입력
driver.find_element(By.CLASS_NAME, value='bt_search').send_keys(Keys.ENTER) # 서치 버튼 찾아서 엔터

# Xpath 사용
driver.find_element(By.XPATH, value='//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a').click()

# 스크롤 다운 방법
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # 자바스크립트 스크립트 사용
# driver.find_element()By.TAG_NAME, value='body').send_keys(Keys.PAGE_DOWN) # find_element 사용

# 스크롤을 가장 끝까지 내리는 코드 작성
prev_height = driver.execute_script('return document.body.scrollHeight') # 현재의 페이지 높이
prev_height

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # 스크롤 다운하는 자바스크립트 사용
    time.sleep(2) # 스크롤을 내린 후, 2초간 로딩할 시간을 줌
    
    curr_height = driver.execute_script('return document.body.scrollHeight') # 현재 페이지의 높이 저장
    if curr_height == prev_height:
        break
    prev_height = curr_height # 기존 높이와 현재 높이가 같아질 때까지 실행 -> 스크롤 다운이 끝까지 진행 시 같아짐

# 스크롤 다운한 페이지 제목 스크래핑
    
html = BeautifulSoup(driver.page_source) # html을 BS객체로 변환
txt = html.select('div.title_area > a') # 관련 태크 영역 모두 선택
txt[0].text # 리스트 첫번째 요소 텍스트 추출 확인

txt_list = [i.text for i in txt] # 리스트 내포문을 이용해 추출

driver.quit()







