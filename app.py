from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from consent import ConsentForm, create_form
from flask import redirect, url_for
from flask import request
from hashlib import md5 as hash_fn

from wtforms import StringField, SubmitField, BooleanField, RadioField

users = {}
user_list = ['Parth Jindal', 'Neha Dalmia', 'Suhas Jain',
             'Pranav Rajput', 'Rajat Bachawat', 'Animesh Jha']


questions = {
    "q1": {
        "question": "What is your name?",
        "response_type": "text",
        "options": [],
    },
    "q2": {
        "question": "What is your age?",
        "response_type": "number",
        "options": [],
    },
    "radio3": {
        "question": "How comfortable are you with the following?",
        "response_type": "radio",
        "options": ["Very comfortable", "Somewhat comfortable", "Not comfortable"],
    },
    "radio4": {
        "question": "What are your hobbies?",
        "response_type": "checkbox",
        "options": ["Reading", "Writing", "Coding", "Gaming", "Sports"],
    },
}


def hash_users():
    for i, user in enumerate(user_list):
        hash_val = hash_fn(str(i).encode()).hexdigest()
        hash_val = hash_val[:8]
        users[hash_val] = user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html", name="Parth", date="12/12/2019")


@app.route("/hello")
def hello_world():
    return 'hello world'


@app.route("/hello/<name>")
def varfunc(name):
    return 'Hello %s, Adios !' % name


@app.route('/survey/<id>', methods=['GET', 'POST'])
def index(id):
    name = users[id]
    form = ConsentForm()
    if request.method == 'POST':
        if form.is_submitted():
            if form.accept.data == "Yes":
                return redirect(url_for('survey2', id=id))
            else:
                return redirect(url_for('varfunc', name=name))
    return render_template('consent_form.html', form=form, name=name)


@app.route("/survey2/<id>", methods=['GET', 'POST'])
def survey2(id):
    if (request.method == 'POST'):
        return redirect(url_for('varfunc', name=users[id]))
    form, fields = create_form(questions=questions)
    return render_template('survey2.html', form=form, questions=fields)


if __name__ == '__main__':
    hash_users()
    print(users)
    app.run(debug=True)
