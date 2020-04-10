import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190602'
html = requests.get(url)
# print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
# div 의 class 가 info-movie 인 것들을 모두 가져온다 (영화정보)
title_list = soup.select('div.info-movie')

for i in title_list:
    # 영화 정보 중에서 <a><strong>인것 하나를 가져온후
    # text만 출력하고 앞뒤 공백을 제거한다
    print(i.select_one('a > strong').text.strip())
