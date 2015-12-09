import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def other():
    return 'Main Application Page! add: /hello to see another page!'

@app.route('/hello')
def hello():
    list = [
        {'message': 'Hello World!!'},
        {'test':'Test hello world.'}
    ]
    results = jsonify(results=list)
    list2 = [
        {'success': results},
        {'error': 'INSERT ERROR MESSAGE'}
    ]
    return jsonify(results=list2)

if __name__ == '__main__':
    app.run()
