from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from consent import ConsentForm, create_form, MCQ
from flask import redirect, url_for
from flask import request
from hashlib import md5 as hash_fn
from wtforms import StringField, SubmitField, BooleanField, RadioField
from downloader import download_file_from_google_drive
from questions import questions
from specific_question_generator import *
from generator import *
from specific_survey import *
import csv
from flask_login import current_user
from collections import OrderedDict
from copy import deepcopy

users = {}


user_list = ['Parth Jindal', 'Neha Dalmia', 'Suhas Jain',
             'Pranav Rajput', 'Rajat Bachawat', 'Animesh Jha']

GENERAL_SURVEY_OUTPUT = "output.csv"
TOTAL_GENERAL_QS = 63


def hash_users():
    for i, user in enumerate(user_list):
        hash_val = hash_fn(str(i).encode()).hexdigest()
        hash_val = hash_val[:8]
        users[hash_val] = {
            "name": user,
        }


def parselink(linkstring):
    arr = linkstring.split('/')

    return arr[-2]


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


@app.route("/gateway/<id>", methods=['GET', 'POST'])
def inbetween(id):
    if request.method == 'POST':
        data = request.form["Question"]
        file_id = parselink(data)
        download_file_from_google_drive(file_id, "zips/"+file_id+".zip")
        users[id]["file_id"] = file_id
        return redirect(url_for('survey3', id=id))
    # redirect(url_for('specific survey', params = final_qs)) #, id = id))
    return render_template("guide.html")
   # return render_template('guide.html', ) #, first_sentence = "This is meant to be a guide for %s made by pranav\n" % name)


@app.route("/hello/<name>/final")
def varfun2(name):
    return "Hope to see you soon %s !" % name


@app.route('/survey/<id>', methods=['GET', 'POST'])
def index(id):
    name = users[id]["name"]
    form = ConsentForm()
    if request.method == 'POST':
        if form.is_submitted():
            if form.accept.data == "Yes":
                return redirect(url_for('survey2', id=id))
            else:
                return redirect(url_for('varfunc', name=name))
    return render_template('consent_form.html', form=form, name=name)


user_choices = {}


@app.route("/survey2/<id>", methods=['GET', 'POST'])
def survey2(id):
    form, fields = create_form(questions=questions)
    if (request.method == 'POST') and form.is_submitted():
        print(form.data)
        form_data = []
        for field in fields:
            if (isinstance(form[field], MCQ)):
                val = ""
                for i in range(len(form[field].choices)):
                    if i+1 in form[field].data:
                        val += "1"
                    else:
                        val += "0"
                form_data.append(val)
            else:
                form_data.append(form[field].data)

        with open("output.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(form_data)
        return redirect(url_for('inbetween', id=id))
    for field in fields:
        if (isinstance(form[field], MCQ)):
            form[field].data = []
    return render_template('survey2.html', form=form, questions=fields)


@ app.route("/survey3/<id>", methods=['GET', 'POST'])
def survey3(id):
    name = users[id]["name"]
    file_id = users[id]["file_id"]

    indices, trans = generate_qs(file_id)
    specific_survey_questions = {}

    for ind in range(0, len(indices)):
        if (trans[indices[ind]] == ""):
            continue
        question_set = func([indices[ind]])
        questions_formatted = generate_q_list(
            question_set, trans[indices[ind]])
        for key, val in questions_formatted.items():
            new_key = "q-" + str(indices[ind]) + "-" + str(key[1:]).zfill(2)
            specific_survey_questions[new_key] = val

    for i in range(0, 11):
        key = "q-" + str(i) + "-01"
        check_val = specific_survey_questions.get(key)
        if (check_val is not None):
            new_key = "q-" + str(i) + "-00"
            specific_survey_questions[new_key] = deepcopy(
                specific_survey_questions[key])
            data_entry = specific_survey_questions[key]["attribute"]
            specific_survey_questions[new_key]["question"] = "Amount: {}, Paid to: {}, Date and Time: {}".format(
                data_entry[1], data_entry[2], data_entry[4])
            specific_survey_questions[new_key]["response_type"] = "text"

    form, fields = create_form(questions=specific_survey_questions)
    indices = {}
    ctr = 1
    for field in fields:
        if field == "submit":
            continue
        if (field.split("-")[2] != "00"):
            indices[field] = ctr
            ctr += 1

    if (request.method == 'POST'):
        form_data = []
        for field in fields:
            form_data.append(form[field].data)
        with open("output2.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(form_data)
        return redirect(url_for('varfunc2', name=name))
    return render_template('specific_survey.html', form=form, questions=fields, indices=indices)


if __name__ == '__main__':
    hash_users()
    print(users)
    with open(GENERAL_SURVEY_OUTPUT, 'w') as csvfile:
        fieldnames = ["Name"]
        for i in range(TOTAL_GENERAL_QS):
            fieldnames.append("Q" + str(i + 1))
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    app.run(debug=True)
