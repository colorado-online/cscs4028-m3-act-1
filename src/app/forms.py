'''
CSC 4028 - Software Security Testing
Student:
Description: M3 Activity 1
'''

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired

# TODO #2: complete the recipe form with the missing fields (title, type, and tags)
class RecipeForm(FlaskForm):
    number = StringField('Recipe#', validators=[DataRequired()])
    submit = SubmitField('Submit')