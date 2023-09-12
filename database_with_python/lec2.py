import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_mail='another@gmail.com'
new_phone=input("plz eneter a phone no.")

#update_sql="UPDATE contacts SET email='{}' WHERE contacts.phone ='{}'".format(new_mail,new_phone)
update_sql="UPDATE contacts SET email=? WHERE phone =?"  #.format(new_mail,new_phone)
update_cursor=db.cursor() #cursor is using the cconnection stored in db 
update_cursor.execute(update_sql,(new_mail,new_phone))
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()


for name,phone,email in db.execute("SELECT * FROM contacts "):
    print(name)
    print(phone)
    print(email)
    print("-"*10)

db.close()