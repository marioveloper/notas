import sqlite3
#Connecting to sqlite
conn = sqlite3.connect('users.db')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
sql ='''CREATE TABLE user(
    id CHAR(20),
    firstname CHAR(40),
    username CHAR(40),
    chat_id CHAR(40),
    chat_type CHAR(40),
    has_private_forwards CHAR(40),
    invite_link CHAR(100),
    saldo int,
    numero_telefonico CHAR(20),
    tarjeta CHAR(20)
    )'''
cursor.execute(sql)
print("Table created successfully........")
# Commit your changes in the database
conn.commit()
#Closing the connection
conn.close()

