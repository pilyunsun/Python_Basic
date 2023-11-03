# **다음 실시간 뉴스 기사 수집기**
#내용: 다음 실시간 뉴스 목록(list: 15개)에서 URL을 추출
#   -> 15개 URL
#   -> 각 url별로 기사 제목, 본문, 날짜 수집
import requests                                 #전체 소스코드
from  bs4 import  BeautifulSoup                 #원하는 정보 select
from service.service_news import get_news
count =0
url = "https://news.daum.net/breakingnews/digital"
result = requests.get(url)

if result.status_code == 200:
    print(result, "접속 성공 -> 데이터를 수집합니다")
    doc = BeautifulSoup(result.text,"html.parser")
    url_list = doc.select("ul.list_news2 a.link_txt")
    for url in url_list:
        count += 1
        print(count, end=' ')
        print("="*100)
        # get_news(): 기사 제목, 본문, 날짜 수집
        get_news(url["href"])
        print(url["href"])
else:
    print("URL 경로가 잘못됬습니다. 확인부탁드립니다.")
