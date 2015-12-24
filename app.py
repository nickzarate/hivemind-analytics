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

#GET
@app.route('/question')
def question(category):
  return 'random question of type {category} from the question bank'

#GET && POST
@app.route('/classes/<string:classname>')
def create(classname):
  return 'create an object in the Parse database'

#GET && DELETE
@app.route('/classes/<string:classname>/<string:objectId>')
def retrieve(classname, objectId):
  return 'retrieve/delete the object with the specified classname and object ID'

#GET && POST
@app.route('/users')
def signup():
  return 'query/sign up a new user'

#GET
@app.route('/login')
def login():
  return 'login user'

#GET
@app.route('/users/me')
def currentUser():
  return 'current user'

@app.route('/')

@app.errorhandler(404)
def page_not_found(e):
  return 'page not found'


@app.route('/answerhistory-r')
def get_answer_history_r():

  payload = {
    'X-Parse-Application-Id': APPLICATION_ID,
    'X-Parse-REST-API-Key': REST_API_KEY
  }

  response = requests.get("http://api.parse.com/1/classes/AnswerHistory/", params = payload)
  return response.json()


@app.route('/answerhistory')
def get_answer_history():
  connection = httplib.HTTPSConnection('api.parse.com', 443)
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
  