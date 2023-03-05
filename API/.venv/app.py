from flask import Flask
import mysql.connector

app= Flask(__name__)
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
cursor1=conexion1.cursor()

cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close() 