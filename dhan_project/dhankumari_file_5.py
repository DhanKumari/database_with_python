import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="college"
)

mycursor = mydb.cursor()

sql="DELETE FROM Teacher "
mycursor.execute(sql)
mydb.commit()