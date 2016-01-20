from flask import Flask
from make_json_app import make_json_app
app = make_json_app(__name__)
import hivemind.views
import hivemind.api_v1
