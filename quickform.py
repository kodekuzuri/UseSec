from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, IntegerField, FormField, FieldList, SelectField, TextAreaField
from wtforms.validators import DataRequired
from wtforms import widgets

def QuickForm():
    accept = TextAreaField("Please enter the drive link requested by uploading ",)
    submit = SubmitField()