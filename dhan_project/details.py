import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="details"
)

mycursor = mydb.cursor()

# Check if tables exist, create a empty list 
table_names = []

mycursor.execute("SHOW TABLES")

for x in mycursor:
    table_names.append(x[0])

print("printing tables before running the queries: ",table_names)

if "teacher" not in table_names:
    mycursor.execute("CREATE TABLE teacher(name varchar(20), dept varchar(30), phone INT(20))")

if "student" not in table_names:
    mycursor.execute("CREATE TABLE student(name varchar(20), dept varchar(30), rollno INT(10))")

if "department" not in table_names:
    mycursor.execute("CREATE TABLE department(dept_name varchar(20), course varchar(20), no_of_students INT(20), lec_per_week INT(20))")

if "rina" not in table_names:
    mycursor.execute("CREATE TABLE rina (name varchar(20), dept varchar(30), phone INT(20))")

mydb.commit()

#printing the tables after running the if statements 
print("{} is already present".format(table_names))

mycursor.close()
mydb.close()
    


