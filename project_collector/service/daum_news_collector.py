# DAUM NEWS COLLECTOR ver 1.0
# - 작성일자: 2023년11월08일
# - 작성자: pilyun
# - 내용: 사용자가 수집하고 싶은 뉴스 카테고리를 설정하면 해당 카테고리의 실시간 뉴스 기사와 제목을 수집하는 프로그램
# - 라이브러리: requests, beautifulsoup4,pymongo

import requests  # 전체 소스코드
from bs4 import BeautifulSoup  # 원하는 정보 select

#from service.service_news import get_news
count = 0  # 전체 기사수
page = 1  # 시작 페이지 1로 고정


print("="*100)
print("MSG: 수집하고 싶은 뉴스 카테고리를 입력해주세요.")
category = input("> 카테고리: ")
print("= 1.사회")
print("= 2.정치")
print("= 3.경제")
print("= 4.국제")
print("= 5.문화")
print("= 6.연예")
print("= 7.스포츠")
print("= 8.IT")

dict_news = {
    "사회": "sosiety",
    "정치": "politics",
    "경제": "economic",
    "국제": "foreign",
    "문화": "culture",
    "연예": "entertain",
    "스포츠": "sports",
    "IT": "digital"
}
while True:
    url = f"https://news.daum.net/breakingnews/digital?page={page}"
    category = input("= > 카테고리:")
    if category in list(dict_news.keys()):
        break
    else:
        print("= MSG: 올바른 카테고리를 입력해주세요")
    print(list(dict_news.keys()))
    exit()
category = input("= > 카테고리: ")
print(f"replace: {dict_news[category]}")
exit()
page = 0
while True:
    url = f"https://news.daum.net/breakingnews/digital?page={page}"
    if result.status_code == 200:
        print(result, "접속 성공 -> 데이터를 수집합니다")
        doc = BeautifulSoup(result.text,"html.parser")
        url_list = doc.select("ul.list_news2 a.link_txt")
        for url in url_list:
            count += 1
            print(count, end=' ')
            print("="*100)
            # get_news(): 기사 제목, 본문, 날짜 수집
            # get_news(url["href"])
            print(url["href"])
    else:
        print("URL 경로가 잘못됬습니다. 확인부탁드립니다.")

    page += 1

