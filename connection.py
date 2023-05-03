import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",#ip adresi yazılır. şuan yerel server yazılı
    user = "root",
    password = "root",
    database = "mydatabase"
)


mycursor = mydb.cursor()
""" 
Yeni bir veritabanı oluşturmak için
mycursor.execute("CREATE DATABASE mydatabase")

tablo ekleme
mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")
"""

