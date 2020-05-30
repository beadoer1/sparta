import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbsparta                     

# User-Agent가 의미하는 바를 모르겠습니다. 이것도 바꿔줘야 할까요??
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'} 
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML.parser 의 의미하는 바도 모르겠네요. 이것도 변경이 필요한가요??
soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# songs (tr들) 의 반복문을 돌리기
for song in songs:
    # song 안에 a 가 있으면,
    a_tag = song.select_one('td.info > a.title ellipsis')
    if a_tag is not None:
        rank = song.select_one('td.number').text                    # td 중 Class=number의 test 불러옴
        title = a_tag.text                                          # a 태그 사이의 텍스트를 가져오기
        star = song.select_one('td.info > a.artist ellipsis').text  # a 태그 사이의 텍스트를 가져오기
        print(rank,title,star)
        # doc = {
        #     'rank' : rank,
        #     'title' : title,
        #     'star' : star
        # }
        # db.songs.insert_one(doc) # songs에 넣었다!