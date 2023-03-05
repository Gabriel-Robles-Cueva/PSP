from flask import Flask, request
import urllib.request
import urllib.error
import json
import re

app= Flask(__name__)

lista= [{'Gabriel': '1234'},{'Adrian': '5678'},{'Andres': '9999'},{'Vinicio': '0000'}]

@app.route('/login', methods= ['POST'])
def login():
    try:
        params= request.get_data()
        print(params)
    except urllib.error.HTTPError as err:
        print(err.code)
    
@app.route('/get-user', methods=['GET'])
def getUser():
    try:
        args= request.args
        nombre = args.get('nombre')
        
        for i in lista:
            result= {key: value for key, value in i.items() if key == nombre}

        return result
    except urllib.error.HTTPError as err:
        print(err.code)


    
@app.route('/new-user')
def newUser(username,password,email,dni,premiun):
    try:
        return
    except urllib.error.HTTPError as err:
        print(err.code)
    
@app.route('/get-all-users')
def getAllUsers():
    return json.dumps(lista)