from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, IntegerField, FormField, FieldList
from wtforms.validators import DataRequired


class ConsentForm(FlaskForm):
    accept = RadioField("Please indicate consent before proceeding", choices=[
                        ('Yes', 'I consent'), ('No', 'I do not consent')], validators=[DataRequired()])
    submit = SubmitField('Submit')


def create_form(questions):
    fields = []
    class SurveyForm(FlaskForm):
        pass

    for key, value in questions.items():
        if value["response_type"] == "text":
            setattr(SurveyForm, key, StringField(
                value["question"], validators=[DataRequired()]))
        elif value["response_type"] == "number":
            setattr(SurveyForm, key, StringField(
                value["question"], validators=[DataRequired()]))
        elif value["response_type"] == "radio":
            setattr(SurveyForm, key, RadioField(
                value["question"], choices=value["options"], validators=[DataRequired()]))
        fields.append(key)
    setattr(SurveyForm, "submit", SubmitField('Submit'))
    fields.append("submit")
    return SurveyForm(), fields
