from flask import render_template, send_from_directory
from hivemind import app
from os import path, pardir
from os.path import abspath, join, dirname

@app.route('/')
def landing():
  base = abspath(join(dirname(__file__), pardir))
  assets = join(base, 'hivemind/client')
  return send_from_directory(assets, 'index.html')

@app.route('/js/<path:path>')
def send_js(path):
  base = abspath(join(dirname(__file__), pardir))
  assets = join(base, 'hivemind/client/js')
  return send_from_directory(assets, path)

@app.route('/css/<path:path>')
def send_css(path):
  base = abspath(join(dirname(__file__), pardir))
  assets = join(base, 'hivemind/client/css')
  return send_from_directory(assets, path)
