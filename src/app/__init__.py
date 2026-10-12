'''
CSC 4028 - Software Security Testing
Student:
Description: M3 Activity 1
'''

from flask import Flask

app = Flask('Recipes Web App')

# consider using an ENVIRONMENT VARIABLE to improve security
app.secret_key = 'you-will-never-guess'

from app import routes