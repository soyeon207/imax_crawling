# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import telegram
from bs4 import BeautifulSoup

bot = telegram.Bot(token = '1181502709:AAESeEpf46yrKkyKdIvTH2cUdbtDgySAM-w')

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190530'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
imax = soup.select_one('span.imax');

if(imax):
    imax = imax.find_parent('div',class_='col-times')
    title = imax.select_one('div.info-movie>a>strong').text.strip()
    bot.sendMessage(chat_id=1053225234, text=title+" IMAX 영화 예매가 열렸습니다")
else:
    bot.sendMessage(chat_id=1053225234, text=" IMAX 영화가 아직 열리지 않았습니다")
