from flask import Flask
from hivemind.make_json_app import make_json_app
app = Flask(__name__)
import hivemind.views
import hivemind.api_v1
