from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
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

#-------------------------------------------------POST--------------------------------------------------------------
@app.route('/add-object')
def añadirObjeto():
    cur2= mysql.connection.cursor()
    cur2.execute('SELECT * FROM objetos ORDER BY 4, 5')
    data= cur2.fetchall()
    return render_template('añadir.html', objetos= data)

@app.route('/object-added', methods=['POST'])
def objetoAñadido():
    if request.method == 'POST':
        nombre= request.form['nombre']
        desc= request.form['desc']
        tipo= request.form['tipo']
        precio= request.form['precio']
        cur= mysql.connection.cursor()
        cur.execute('INSERT INTO objetos (nombre,descripcion,tipo,precio) VALUES (%s, %s, %s, %s)', (nombre,desc,tipo,precio))
        mysql.connection.commit()
        flash('Objeto añadido correctamente')
        return redirect(url_for('añadirObjeto'))

#-------------------------------------------------GET--------------------------------------------------------------
@app.route('/get-objects', methods=['GET'])
def verObjetos():
    cur2= mysql.connection.cursor()
    cur2.execute('SELECT * FROM objetos')
    data= cur2.fetchall()
    return jsonify(data)

#-------------------------------------------------PUT--------------------------------------------------------------
@app.route('/edit-object')
def editarObjeto():
    return 'edit_object'

#-------------------------------------------------DELETE--------------------------------------------------------------
@app.route('/delete-object/<string:id>')
def eliminarObjetoByID(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM objetos WHERE id = {}'.format(id))
    mysql.connection.commit()
    flash('Objeto borrado correctamente')
    return redirect(url_for('añadirObjeto'))

@app.route('/delete-object-name')
def eliminarObjetoByName():
    return render_template('borrar.html')


if __name__=='__main__':
    app.run(port = 3000, debug= True)