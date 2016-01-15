from hivemind import app

@app.route('/')
def hello_world():
    return 'Thank you for your patronage. Have a nice day.'

