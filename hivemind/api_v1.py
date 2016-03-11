from flask import jsonify, abort, request
import json, httplib, array

from hivemind import app
from algorithms import phi_ols_estimator

root = '/api/v1'

@app.route(root + '/echo', methods=['GET'])
def api_echo():
  return jsonify(
    payload = 'hi'
  )

@app.route(root + '/get_phi', methods=['GET','PUT','POST']) # SKETCHY AF
def get_phi():
  payload = request.get_json()
  print payload
  covariates = payload[u'covariates']
  p = payload[u'p']
  phi = phi_ols_estimator(covariates, p)
  return jsonify(
    phi = phi.tolist()
  )
