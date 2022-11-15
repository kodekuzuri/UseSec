from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from consent import ConsentForm
from flask import redirect,url_for

from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'   
Bootstrap(app)

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html", name = "Parth",date="12/12/2019")

@app.route("/hello")
def hello_world():
    return 'hello world' 

@app.route("/hello/<name>")
def varfunc(name):
    return 'Hello %s, Adios !' % name 

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ConsentForm()
    if request.method == 'POST':
        if form.is_submitted():
            if form.accept.data == "Yes":
                return redirect(url_for('home'))
            else:
                return redirect(url_for('varfunc', name = "Parth"))
    return render_template('consent_form.html', form=form)

if __name__ == '__main__':
    app.run(debug = True) ; 