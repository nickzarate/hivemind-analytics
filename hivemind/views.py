from flask import render_template, send_from_directory, redirect, request, url_for
from hivemind import app
from os import path, pardir
from os.path import abspath, join, dirname

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def landing(path):
  base = abspath(join(dirname(__file__), pardir))
  assets = join(base, 'hivemind/static')
  return send_from_directory(assets, 'index.html')

@app.route('/js/<path:path>')
def send_js(path):
  base = abspath(join(dirname(__file__), pardir))
  assets = join(base, 'hivemind/static/js')
  return send_from_directory(assets, path)

@app.route('/css/<path:path>')
def send_css(path):
  base = abspath(join(dirname(__file__), pardir))
  assets = join(base, 'hivemind/static/css')
  return send_from_directory(assets, path)
