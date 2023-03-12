from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
tipos= ["Pokeball", "Equipable", "Curacion", "Bayas", "Combate", "MT"]
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

#-----------------------------------------------------GET-----------------------------------------#

@app.route('/get-objects', methods=['GET'])
def verObjetos():
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM objetos')
    data= cur.fetchall()
    
    columns = [desc[0] for desc in cur.description]

    results = []
    for row in data:
        row_dict = {}
        for i in range(len(columns)):
            row_dict[columns[i]] = row[i]
        results.append(row_dict)
        
    return jsonify(results)

@app.route('/get-objects-by-name', methods=['GET'])
def verObjetosPorNombre():
    name = request.args.get('nombre')
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM objetos WHERE nombre=%s', (name,))
    data = cur.fetchall()
    if len(data) == 0:
        flash('404 Not Found- Existe Un Objeto Con Ese Nombre')
        return redirect(url_for('inicio'))

    columns = [desc[0] for desc in cur.description]

    results = []
    for row in data:
        row_dict = {}
        for i in range(len(columns)):
            row_dict[columns[i]] = row[i]
        results.append(row_dict)

    return jsonify(results)

@app.route('/get-objects-by-tipo', methods=['GET'])
def verObjetosPorTipo():
    tipo = request.args.get('tipo')
    if tipo not in tipos:
        flash('400 Bad Request- Tipo no valido')
        return redirect(url_for('inicio'))
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM objetos WHERE tipo=%s', (tipo,))
    data = cur.fetchall()

    columns = [desc[0] for desc in cur.description]

    results = []
    for row in data:
        row_dict = {}
        for i in range(len(columns)):
            row_dict[columns[i]] = row[i]
        results.append(row_dict)

    return jsonify(results)

#-----------------------------------------------------POST-----------------------------------------#
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
        cur.execute('INSERT INTO objetos (`NOMBRE`, `OBJ_DESCRIPCION`, `TIPO`, `PRECIO`) VALUES (%s, %s, %s, %s)', (nombre,desc,tipo,precio))
        mysql.connection.commit()
        flash('Objeto añadido correctamente')
        return redirect(url_for('añadirObjeto'))
    
#-----------------------------------------------------DELETE-----------------------------------------#
@app.route('/delete-object/<string:id>')
def eliminarObjetoByID(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM objetos WHERE id = {}'.format(id))
    mysql.connection.commit()
    flash('Objeto borrado correctamente')
    return redirect(url_for('añadirObjeto'))

@app.route('/delete-object-by-name', methods=['DELETE', 'GET'])
def borrarObjetoPorNombre():
    name = request.args.get('nombre')
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM objetos WHERE nombre = %s', (name,))
    data = cur.fetchall()
    if len(data) == 0:
        flash('404 Not Found-No Existe Un Objeto Con Ese Nombre')
        return redirect(url_for('inicio'))
    cur2 = mysql.connection.cursor()
    cur2.execute('DELETE FROM objetos WHERE nombre=%s', (name,))
    mysql.connection.commit()
    flash('Objeto borrado correctamente')
    return redirect(url_for('inicio'))

#-----------------------------------------------------PUT-----------------------------------------#
@app.route('/edit-object-type', methods=['PUT', 'GET'])
def editarObjeto():
    id = request.args.get('id')
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM objetos WHERE id = {}'.format(id))
    data = cur.fetchall()
    if len(data) == 0:
        flash('404 Not Found-No Existe Un Objeto Con Ese ID')
        return redirect(url_for('inicio'))
    else:
        tipo = request.args.get('tipo')
        if tipo not in tipos:
            flash('400 Bad Request- Tipo no valido')
            return redirect(url_for('inicio'))
        else:
            cur.execute('UPDATE objetos SET TIPO=%s WHERE id=%s', (tipo, id))
            mysql.connection.commit()
            flash('Objeto editado correctamente')
            return redirect(url_for('inicio'))
    
@app.route('/edit-object-price', methods=['PUT', 'GET'])
def editarObjetoPorPrecio():
    id = request.args.get('id')
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM objetos WHERE id = {}'.format(id))
    data = cur.fetchall()
    if len(data) == 0:
        flash('404 Not Found- Existe Un Objeto Con Ese ID')
        return redirect(url_for('inicio'))
    else:
        precio = request.args.get('precio')
        try:
            prueba= int(precio)
            cur.execute('UPDATE objetos SET PRECIO=%s WHERE id=%s', (precio, id))
            mysql.connection.commit()
            flash('Objeto editado correctamente')
            return redirect(url_for('inicio'))
        except:
            flash('400 Bad Request- Precio no valido')
            return redirect(url_for('inicio'))
            