import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def other():
    return 'Main Application Page! add: /hello to see another page!'

@app.route('/hello')
def helloWorld():
    list = [
        {'message': 'Hello World!!'},
        {'test':'Test hello world.'}
    ]
    results = jsonify(results=list)
    list2 = [
        {'success': results},
        {'error': 'INSERT ERROR MESSAGE'}
    ]
    return {'success': 'Hello World!!'}

if __name__ == '__main__':
    app.run()
