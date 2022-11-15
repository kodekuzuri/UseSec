from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class ConsentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    accept = BooleanField('I accept the terms and conditions', validators=[DataRequired()])
    submit = SubmitField('Submit')