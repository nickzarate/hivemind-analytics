from flask import Flask

@app.route('/')
def hello_world():
  return 'Hello World!'

application = Flask(__name__)

if __name__ == "__main__":
  application.debug = True
  application.run()
