import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('users.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

queryCreateUser ='''CREATE TABLE user(
    id VARCHAR(20),
    firstname VARCHAR(40),
    username VARCHAR(40),
    referred_by VARCHAR(20),
    invite_link VARCHAR(100),
    rank VARCHAR(40),
    wallet VARCHAR(100),
    referrals INT DEFAULT 0,
    status INT DEFAULT 0,
    PRIMARY KEY("id")
    )'''


queryCreateInvestment = '''CREATE TABLE investments(
	id	INTEGER NOT NULL,
	date	datetime,
	user_id	VARCHAR(20),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "users"("id")
)'''

cursor.execute(queryCreateUser)
cursor.execute(queryCreateInvestment)

print("Table created successfully........")

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()

