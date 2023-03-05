from flask import Flask

app= Flask(__name__)

class Usuario():
    def __init__(self, name, password, birthdate):
        self.name= name
        self.password= password
        self.birthdate= birthdate

usuarios= []

@app.post('/user/<name>/<password>/<birthdate>')
def registrarUser(name,password,birthdate):
    user= Usuario(name,password,birthdate)
    usuarios.append(user)
    
@app.route('/user')
def getUsers():
    return usuarios