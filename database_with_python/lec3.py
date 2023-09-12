#show all data base present
import sqlite3
aa = sqlite3.connect("contacts.sqlite")

name=input("plz entera name ")
#for row in aa.execute("SELECT * FROM contacts WHERE name = ?",(name,)):
for row in aa.execute("SELECT * FROM contacts WHERE name LIKE ?",(name,)):
    print(row)


aa.close( )


