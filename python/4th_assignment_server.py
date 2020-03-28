from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbpeter                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index_order.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name']
    count_receive = request.form['count']
    address_receive = request.form['address']
    phone_receive = request.form['phone']
    # 2. DB에 정보 삽입하기
    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.orders.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 완료되었습니다.'})

@app.route('/orders', methods=['GET'])
def read_orders():
    send_data = []
    all_orders = list(db.orders.find())
    for order in all_orders:
        send_data.append({
            'name' : order['name'],
            'count' : order['count'],
            'address' : order['address'],
            'phone': order['phone']
        })
    return jsonify({'result':'success', 'data': send_data, 'msg': '이 요청은 GET!'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)