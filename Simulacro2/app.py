from flask import Flask

app= Flask(__name__)

@app.route('/<username>')
def getUser(username):
    return username

@app.post('/newuser')
def getNewUser():
    diccionario= {
        "nombre": "Aja"
}
