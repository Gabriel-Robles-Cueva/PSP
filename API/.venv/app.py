from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#MySQL Connection
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'db_objetos'
mysql = MySQL(app)

#Setting
app.secret_key= 'mysecretkey'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/add-object')
def añadirObjeto():
    return render_template('añadir.html')

@app.route('/object-added', methods=['POST'])
def objetoAñadido():
    if request.method == 'POST':
        nombre= request.form['nombre']
        tipo= request.form['tipo']
        precio= request.form['precio']
        print(nombre)
        print(tipo)
        print(precio)
        cur= mysql.connection.cursor()
        cur.execute('INSERT INTO objetos (nombre,tipo,precio) VALUES (%s, %s, %s)', (nombre,tipo,precio))
        mysql.connection.commit()
        flash('Objeto añadido correctamente')
        return redirect(url_for('añadirObjeto'))

@app.route('/get')
def verObjetos():
    return 'see_object'

@app.route('/edit')
def editarObjeto():
    return 'edit_object'

@app.route('/delete')
def eliminarObjeto():
    return 'delete-object'

if __name__=='__main__':
    app.run(port = 3000, debug= True)