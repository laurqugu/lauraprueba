import json
from json import loads
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
#from flask_mysqldb import MySQL


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQL_ALCHEMY_DATABASE_URI']='mysql+pymsql://root@localhost/prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Primos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)

    def __init__(self, numero):
        self.numero

class PrimosPares(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)

    def __init__(self, numero):
        self.numero


@app.route('/primos/<int:numero>', methods=['GET'])
def numeros_primos(numero):
    primos = []
    for num in range(2, numero):
        if all(num % i != 0 for i in range(2, num)):
            primos.append(num)

    return make_response(jsonify({'result': primos}), 200)


@app.route('/primosGemelos/<int:numero>', methods=['GET'])
def primos_gemelos(numero):
    primos = []
    for num in range(2, numero):
        if all(num % i != 0 for i in range(2, num)):
            primos.append(num)

    primos_gemelos = []
    for p in primos:
        par = p + 2
        if par in primos:
            primos_gemelos.extend([p, par])

    return make_response(jsonify({'result': primos_gemelos}), 200)


@app.route('/primosBd/<int:numero>', methods=['GET'])
def primos_bd(numero):
    primos = []
    for num in range(2, numero):
        if all(num % i != 0 for i in range(2, num)):
            primos.append(num)

    return make_response(jsonify({'result': primos}), 200)

@app.route('/primosGemelosBd/<int:numero>', methods=['GET'])
def primos_pares_db(numero):
    primos = []
    for num in range(2, numero):
        if all(num % i != 0 for i in range(2, num)):
            primos.append(num)

    primos_gemelos = []
    for p in primos:
        par = p + 2
        if par in primos:
            primos_gemelos.extend([p, par])

    return make_response(jsonify({'result': primos_gemelos}), 200)



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
