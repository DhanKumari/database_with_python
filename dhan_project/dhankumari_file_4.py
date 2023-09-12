import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="college"
)

mycursor = mydb.cursor()

#update 
sql1 = ("UPDATE teacher SET dept = %s WHERE name = 'melvin'")
val1=("etc",)
mycursor.execute(sql1,val1)
mydb.commit()

sql2 = ("UPDATE student SET rollno =%s, dept=%s WHERE name = 'ayushman' AND rollno = '12'")
val2=(15,"IT")
mycursor.execute(sql2,val2)
mydb.commit()

sql3 = ("UPDATE department SET deprt_name= %s, course =%s, no_of_studnets=%s,lec_per_week=%s WHERE deprt_name= 'civil '")
val3=("mining","autoCAD",34,5)
mycursor.execute(sql3,val3)
mydb.commit()







