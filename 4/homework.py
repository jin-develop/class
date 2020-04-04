from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('homework4.html')

## API 역할을 하는 부분
@app.route('/users', methods=['POST'])
def write_user():
    # 1. 정보를 잘 받자, 제목, 저자, 리뷰
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    # 2. DB에 저장하자.
    user = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'number': number_receive
    }
    db.users.insert_one(user)
    # 3. 잘 되었음을 클라이언트에 알려주자.

    return jsonify({'result':'success', 'msg': '성공적으로 저장!'})


@app.route('/users', methods=['GET'])
def read_user():
    # 1. 저장된 정보를 가져온다.
    users = list(db.users.find({}, {'_id': False}))
    # 2. 리뷰들을 돌려준다.
    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)