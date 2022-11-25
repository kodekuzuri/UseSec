from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, IntegerField, FormField, FieldList, SelectField, TextAreaField
from wtforms.validators import DataRequired
from wtforms import widgets
import validators
def QuickForm():
    drivelink = TextAreaField("Please enter the drive link requested by uploading ", [validators.optional(), validators.length(max=250)])
    submit = SubmitField()