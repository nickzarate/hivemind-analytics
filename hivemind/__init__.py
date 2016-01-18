from flask import Flask
from make_json_app import make_json_app
app = Flask(__name__)
import hivemind.responses
import hivemind.api_v1
