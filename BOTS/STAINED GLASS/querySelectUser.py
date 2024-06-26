import conexion as conn

db = conn.DB()

querySelectUser = 'SELECT * FROM user'

try:
    table = db.execute_query(querySelectUser)
    filas = table.fetchall()
    for row in filas:
            print("Id: ", row[0])
            print("FirstName: ", row[1])
            print("Username ", row[2])
            print("Referred_by: ", row[3])
            print("Invite_Link: ", row[4])
            print("Rank ",row[5])
            print("Wallet ",row[6])
            print("Referrals ",row[7])
            print("Status ",row[8])
            print("\n")
except ConnectionError as e:
    print(e)
