from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

# 1. 어벤져스: 엔드게임 평을 찾자!
# 힌트: find( {찾는 조건을 여기다 적으세요} )
stars = db.movie.find_one({'title':'어벤져스: 엔드게임'}, {'_id':False})
print(stars['star'])
same = stars['star']
print('*'*70)

# 2.'어벤져스: 엔드게임'의 평점과 같은 평점의 영화 제목들을 가져오기
# 힌트: find( {찾는 조건을 여기다 적으세요} )
sames = list(db.movie.find({'star': same}, {'_id':False}))

for r in sames:
    print(r['title'])

print('*'*70)
# 3. '어벤져스: 엔드게임'의 평점과 같은 평점의 영화 제목들의 평점을 0으로 만들기
# 힌트: update( {찾는 조건을 여기다 적으세요}, { '$set': { 변경 조건을 여기에 적으세요 }} )


db.movie.update_many({'star':same}, {'$set': {'star': 0}})


