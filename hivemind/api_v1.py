from flask import jsonify, abort
import json, httplib, requests

from hivemind import app
from crossdomain import crossdomain


root = '/api/v1'


@app.route(root + '/echo')
@crossdomain(origin='*')
def api_echo():
    print 'sorta'
    return jsonify(
        payload = 'Hello'
    )




###############################################


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

