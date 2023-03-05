from flask import Flask
import json
import re
import mysql.connector

application= Flask(__name__)

class Usuario():
    def __init__(self, name, password, birthdate):
        self.name= name
        self.password= password
        self.birthdate= birthdate

usuarios= {}

@application.route('/user/<name>/<password>/<correo>/<birthdate>')
def registrarUser(name,password,correo,birthdate):
    usuarios["name"]= name
    usuarios["password"]= password
    usuarios["correo"]= correo
    usuarios["nacimiento"]= birthdate
    return json.dumps(usuarios)
    
    
@application.route('/user')
def getUsers():
    return json.dumps(usuarios["name"])+json.dumps(usuarios["nacimiento"])

@application.route('/user/detalles')
def getUsersDetails():
    return json.dumps(usuarios["name"])+json.dumps(usuarios["correo"])+json.dumps(usuarios["nacimiento"])