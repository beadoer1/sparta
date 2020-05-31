import requests
from bs4 import BeautifulSoup
     
from pymongo import MongoClient          
client = MongoClient('localhost', 27017)
db = client.dbsparta 

# User-Agent가 의미하는 바는 뭘까요
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'} 
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML.parser 의 의미하는 바는 뭘까요
soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr') # ★ Copy > Copy selector 를 통해 따올 것!!! ★ 

for song in songs:
    # ★Class 따올 시 공백을 두면 인식이 안되는 듯 하다. '.'으로 처리하여 해결(다른분들 과제 참고)★
    a_tag = song.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        rank = song.select_one('td.number').text[:2].strip()               # td 중 Class=number의 test 불러옴
        title = a_tag.text.strip()                                         # a 태그 사이의 텍스트를 가져오기
        star = song.select_one('td.info > a.artist.ellipsis').text.strip() # a 태그 사이의 텍스트를 가져오기
        print(rank,title,star)
        doc = {
            'rank' : rank,
            'title' : title,
            'star' : star
        }
        db.songs.insert_one(doc) # songs에 등록하기
