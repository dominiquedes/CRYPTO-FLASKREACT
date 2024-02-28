from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_cors import CORS
import uuid
import psycopg2

app = Flask(__name__)
CORS(app, origins='*')

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:03sept08@localhost/cryptoapp"
db = SQLAlchemy(app)


class SavedCoin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coin_id = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Coin Name: {self.name}"
    
    def __init__(self, name, coin_id):
        self.name = name
        self.coin_id = coin_id

@app.route('/coin/<id>', methods = ['GET'])
def get_coin(id):
    coin_id = id 

    response = requests.get(f'https://api.coingecko.com/api/v3/coins/{id}')

    if response.status_code == 200:
        data = response.json()
        return  data
    else:
        return {"message": "Could not get data"}

@app.route('/coin/<id>', methods = ['DELETE'])
def delete_event(id):
    db.session.delete(id)
    db.session.commit()

    return 'Coin unsaved'

@app.route('/add-coins', methods=['POST'])
def add_coin():

    # Handle POST request
    data = request.json
    coin_id = data.get('coin_id')
    coin_name = data.get('name')

    new_coin = SavedCoin(name=coin_name, coin_id=coin_id)
    db.session.add(new_coin)
    db.session.commit()

    return data

@app.route('/coins')
def get_coins():
    url = "https://rest.coinapi.io/v1/assets"
    payload={}
    headers = {
    'Accept': 'text/json',
    'X-CoinAPI-Key': '16476A50-1E62-4BCC-B8BA-FC186235FFB3'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else: 
        print("failed to fetch")

@app.route('/')
def start():
    all_coins = SavedCoin.query.all()
    data_list = [{'id': coin.id, 'coin_id': coin.coin_id, 'name': coin.name} for coin in all_coins]

    response = jsonify(data_list)

    return response

@app.route('/delete-coin', methods=['DELETE'])
def delete_coin():
    data = request.json
    delete_id = data.get('id')

    check_id = SavedCoin.query.filter_by(id=delete_id).first()
    if check_id:
        db.session.delete(check_id)
        db.session.commit()

        return jsonify({"message": "data deleted!"})

if __name__ == '__main__':
    app.run(debug=True)
