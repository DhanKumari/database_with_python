import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="testtt2"
)

mycursor = mydb.cursor()

# Check if tables exist, create a empty list 
table_names = []

mycursor.execute("SHOW TABLES")

for x in mycursor:
    table_names.append(x[0])

if "teacher" in table_names:
    pass
else:
    mycursor.execute("CREATE TABLE teacher(name varchar(20), dept varchar(30), phone INT(20))")

if "shop" in table_names:
    pass
else:
    mycursor.execute("CREATE TABLE shop(name varchar(20), dept varchar(30), phone INT(20))")
    

mydb.commit()

#printing the tables after running the if statements 
print("{} is already present".format(table_names))

mycursor.close()
mydb.close()
