from flask import flask
app = flask(__name__)


@app.route('/')
def my_function():
 return "falai meu bom"