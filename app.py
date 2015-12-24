from flask import Flask
app = Flask(__name__)

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

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
  # app.run()
  