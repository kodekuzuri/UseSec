from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired

class ConsentForm(FlaskForm):
    accept = RadioField("Please indicate consent before proceeding", choices=[('Yes', 'I consent'), ('No', 'I do not consent')], validators=[DataRequired()])
    submit = SubmitField('Submit')