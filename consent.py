from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, IntegerField, FormField, FieldList, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from wtforms import widgets
from collections import OrderedDict

class ConsentForm(FlaskForm):
    accept = RadioField("Please indicate consent before proceeding", choices=[
                        ('Yes', 'I consent'), ('No', 'I do not consent')], validators=[DataRequired()])
    submit = SubmitField('Submit')


class MCQ(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


def create_form(questions):
    fields = []

    class SurveyForm(FlaskForm):
        pass
    questions = OrderedDict(sorted(questions.items()))
    for key,value in questions.items():
        if value["response_type"] == "text":
            setattr(SurveyForm, key, StringField(
                value["question"], validators=[DataRequired()]))
        elif value["response_type"] == "number":
            setattr(SurveyForm, key, StringField(
                value["question"], validators=[DataRequired()]))
        elif value["response_type"] == "radio":
            setattr(SurveyForm, key, RadioField(
                value["question"], choices=value["options"], validators=[DataRequired()]))
        elif value["response_type"] == "checkbox":
            choices = [(option_id, option)
                       for (option_id, option) in enumerate(value["options"])]
            setattr(SurveyForm, key, MCQ(
                value["question"], choices=choices, coerce=int))
        fields.append(key)
    setattr(SurveyForm, "submit", SubmitField('Submit'))
    fields.append("submit")
    return SurveyForm(), fields
