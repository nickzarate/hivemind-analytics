from flask import Flask
app = Flask(__name__)

import requests
from os import environ

APPLICATION_ID = environ['APPLICATION_ID']
REST_API_KEY = environ['REST_API_KEY']


import json,httplib


@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/answerhistory')
def get_answer_history():
  connection = httplib.HTTPSConnection('api.parse.com')
  connection.connect()
  connection.request('GET', '/1/classes/AnswerHistory', '', {
    "X-Parse-Application-Id": APPLICATION_ID,
    "X-Parse-REST-API-Key": REST_API_KEY
    })
  result = json.loads(connection.getresponse().read())
  return json.dumps(result)



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    # app.run()
