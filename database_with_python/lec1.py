import sqlite3
db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE  IF NOT EXISTS contacts ( name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('kannu',2345678,'kannu@gmail.com')")
db.execute("INSERT INTO contacts VALUES('TIM',12445,'yyy@gmailcom')")

cursor= db.cursor() #generator
cursor.execute("SELECT * FROM contacts")
#print(cursor.fetchall())

for row in cursor:
    print(row)

cursor.close()
db.commit()
db.close()