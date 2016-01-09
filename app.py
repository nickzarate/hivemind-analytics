from flask import Flask
from os import environ
import json, httplib, requests

APPLICATION_ID = 'JnIfTyw9Dl4Uq6MDo4uqnhOYwbWPmdrkBuP2NvnK'
REST_API_KEY = '00Ey9OvtSr8nt56g6LKSFdozCPM23GRhF29zgzAN'
app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/answerhistory-r')
def get_answer_history_r():

  payload = {
    'X-Parse-Application-Id': APPLICATION_ID,
    'X-Parse-REST-API-Key': REST_API_KEY
  }

  response = requests.get("http://api.parse.com/1/classes/AnswerHistory/", params = payload)
  return response.json()

@app.route('/test')
def tester():
  return json.dumps(requests.get(url = 'classes/AnswerHistory', params = 0))

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







###############################################

@app.route('/calculate/<string:par1>/<string:par2>/<string:par3>')
def calculate(par1, par2, par3):
  return 'par1: ' + par1 + 'par2: ' + par2 + 'par3: ' + par3

@app.route('/data', methods=['GET','POST'])
def data():
  # here we want to get the value of user (i.e. ?user=some-value)
  user = request.args.get('user')
  thing = request.args.get('thing')
  vector = request.args.get('vector')
  possible = request.get_json()
  print possible
  return user + thing + vector

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
  if not request.json or not 'title' in request.json:
    abort(400)
  task = {
    'id': tasks[-1]['id'] + 1,
    'title': request.json['title'],
    'description': request.json.get('description', ""),
    'done': False
  }
  tasks.append(task)
  return jsonify({'task': task}), 201

@app.route("/json", methods=['GET','POST'])
def json():

    app.logger.debug("JSON received...")
    app.logger.debug(request.json)

    if request.json:
        mydata = request.json # will be 

        return "Thanks. Your age is %s" % mydata.get("age")

    else:
        return "no json received"

@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
  content = request.get_json(silent=True)
  print content
  return uuid

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
  task = [task for task in tasks if task['id'] == task_id]
  if len(task) == 0:
    abort(404)
  if not request.json:
    abort(400)
  if 'title' in request.json and type(request.json['title']) != unicode:
    abort(400)
  if 'description' in request.json and type(request.json['description']) is not unicode:
    abort(400)
  if 'done' in request.json and type(request.json['done']) is not bool:
    abort(400)
  task[0]['title'] = request.json.get('title', task[0]['title'])
  task[0]['description'] = request.json.get('description', task[0]['description'])
  task[0]['done'] = request.json.get('done', task[0]['done'])
  return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
  task = [task for task in tasks if task['id'] == task_id]
  if len(task) == 0:
    abort(404)
  tasks.remove(task[0])
  return jsonify({'result': True})

###############################################


@app.errorhandler(404)
def page_not_found(e):
  return 'page not foundddd!'




if __name__ == "__main__":
  app.debug = True
  app.run(host="0.0.0.0")

