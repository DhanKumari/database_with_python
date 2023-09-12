import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="college"
)

mycursor = mydb.cursor()


sql1 = "INSERT INTO Teacher(name, dept, phone) VALUES(%s,%s,%s)"
val1 = [
    ("kannu", "etc","1234567675"),
    ("melvin", "comp","234588907"),
    ("hrutwa", "etc","345678987"),
    ("neetal", "etc","12567978"),
    ("nishika", "comp","7654321"),
    ("raj", "etc","87658463"),
    ("musatf", "IT","34567890"),
    ("keegan", "etc","15672384"),
]
mycursor.executemany(sql1, val1)
mydb.commit()



sql2 = "INSERT INTO student(name, dept, rollno ) VALUES(%s,%s,%s)"
val2 = [
    ("anish", "IT","1"),
    ("kevin", "comp","2"),
    ("namrata", "IT","3"),
    ("vishvas", "etc","4"),
    ("ajay", "IT","5"),
    ("kiran", "etc","6"),
    ("joan", "IT","7"),
    ("ayushi", "etc","8"),
    ("ajaybind", "IT","9"),
    ("karishma", "IT","10"),
    ("jo", "IT","11"),
    ("ayushman", "etc","12"),
]
mycursor.executemany(sql2, val2)
mydb.commit()



sql3 = "INSERT INTO department(deprt_name, course, no_of_studnets, lec_per_week) VALUES(%s,%s,%s,%s)"
val3 = [("COMP","DA",20,3),
        ("IT","SOFT COMPUTING",23,2),
        ("ETC","WSN",25,4),
        ("ENE","PCB",30,3),
        ("CIVIL","STRUCTURES",35,2),
        ("MECH","MOTORS",15,4),
 
]
mycursor.executemany(sql3, val3)
mydb.commit()