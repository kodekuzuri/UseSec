from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Kill me now :("

@app.route("/hello")
def hello_world():
    return 'hello world' 

@app.route("/hello/<name>")
def varfunc(name):
    return 'Hello %s' % name



if __name__ == '__main__':
    app.run(debug = True) ; 