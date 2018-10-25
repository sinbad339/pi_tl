#-------------------------------------------------------------------------------
# Name:        forms
# Purpose:
#
# Author:      jdilorenzo
#
# Created:     11/09/2018
# Copyright:   (c) jdilorenzo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, BooleanField

from wtforms import validators, ValidationError

class ContactForm(Form):
    name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
    Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
    Address = TextAreaField("Address")

    email = TextField("Email",[validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])

    Age = IntegerField("age")
    language = SelectField('Languages', choices = [('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("Send")

class ConfigureForm(Form):
    mode = RadioField('Mode', choices = [('Traffic Light','Traffic Light'),("Parking Distance",'Parking'),("Sunday at the Speedway",'Sunday at the Speedway'),("Force",'Test')])

    tl_rate = IntegerField("Traffic Light Rate (1 - 100)", validators=[validators.input_required("Required Field"), validators.NumberRange(min=1, max=100)])

    g2y_dist = IntegerField("Green <=> Yellow Distance (inches) (10 - 100)", validators=[validators.input_required("Required Field"), validators.NumberRange(min=10, max=100)])
    y2r_dist = IntegerField("Yellow <=> Red Distance (inches) (10 - 100)", validators=[validators.input_required("Required Field"), validators.NumberRange(min=10, max=100)])
    hyst = IntegerField("Hysteresis (inches) (1 - 5)", validators=[validators.input_required("Required Field"), validators.NumberRange(min=1, max=5)])

    sats_rate = IntegerField("Speedway Rate (1 - 100)", validators=[validators.input_required("Required Field"), validators.NumberRange(min=1, max=100)])

    test_red = BooleanField("Red On", default = False)
    test_yellow = BooleanField("Yellow On", default = False)
    test_green = BooleanField("Green On", default = False)

    submit = SubmitField("Send")
