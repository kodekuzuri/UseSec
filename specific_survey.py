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


def generate_q_list(list_of_q, trans):
   
    questions = {}
    ctr = 0 
    for q in list_of_q:
        ctr = ctr + 1
        q_name = "q" + str(ctr)

        new_q_entry = {
            "question" : q[0],
            "response_type" : "radio",
            "options" : ["Very Uncomfortable", "Uncomfortable", "Neutral", "Comfortable", "Very Comfortable"],
            "receiver" : q[1],
            "transmission_principle": q[2],
            "attribute" : trans[5],
        }

        questions[q_name] = new_q_entry

    return questions





