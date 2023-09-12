import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="college"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT *FROM Teacher LIMIT 5")  ##prints 1st  5 rows
result1 = mycursor.fetchall()

print("\n")
print("printing first 5 rows from Teacher table: ")
for x in result1:
    print(x)
 

mycursor.execute("SELECT *FROM student LIMIT 7")  # prints 1st 7 rows
result2 = mycursor.fetchall()
print("\n")
print("printing first 7 rows from student table:")
for x in result2:
    print(x)


mycursor.execute("SELECT *FROM department ")  # prints all rows
result3 = mycursor.fetchall()
print("\n")
print("printing  rows from department table :")
for x in result3:
    print(x)
