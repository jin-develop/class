from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##
# 1. 제목이 '어벤져스: 엔드게임'인 영화의 평점을 가져오기

movie = db.movie.find_one({'title':'어벤져스: 엔드게임'})
print(movie['star'])

# 2. '어벤져스: 엔드게임'의 평점과 같은 평점의 영화 제목들을 가져오기