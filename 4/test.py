from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
   # 1. 정보를 잘 받자, 제목, 저자, 리뷰

   title_receive = request.form['title_give']
   author_receive = request.form['author_give']
   review_receive = request.form['review_give']

   # 2. DB에 저장하자.
   doc = {
      'title': title_receive,
      'author': author_receive,
      'review': review_receive
   }
   db.reviews.insert_one(doc)
   # 3. 잘 되었음을 클라이언트에 알려주자.
   return jsonify({'result':'success', 'msg': '리뷰가 성공적으로 저장되었습니다.'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    # 1. 저장된 정보를 가져온다.
    reviews = list(db.reviews.find({}, {'_id': False}))

    # 2. 리뷰들을 돌려준다.
    return jsonify({'result':'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)