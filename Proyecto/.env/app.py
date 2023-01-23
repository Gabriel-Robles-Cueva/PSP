from flask import Flask

application= Flask(__name__)

@application.route('/')
def hello_word():
    return "<h1>Hello World</h1>"

@application.route('/usuarios/<username>')
def return_username(username):
    return username

@application.post('/')
def hello_world_post():
    print("Hola desde post")

""" get set post delete """