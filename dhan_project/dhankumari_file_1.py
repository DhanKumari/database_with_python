import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="college"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Teacher(name varchar(20),dept varchar(30),phone INT(20))")


mycursor.execute(
    "CREATE TABLE IF NOT EXISTS student(name varchar(20),dept varchar(30),rollno INT(10))"
)


mycursor.execute(
    "CREATE TABLE IF NOT EXISTS department(deprt_name varchar(20), course varchar(20), no_of_studnets INT(20),lec_per_week INT(20))"
)

























