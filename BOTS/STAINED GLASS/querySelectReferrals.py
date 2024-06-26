import conexion as conn

db = conn.DB()

id = '2345'

querySelectReferrals = 'SELECT firstname, username FROM user WHERE referred_by = ? and status = 0'
parameters = (id,)

try:
    table = db.execute_query(querySelectReferrals, parameters)
    filas = table.fetchall()
    for row in filas:
            print("FirstName: ", row[0])
            print("Username ", row[1])
            print("\n")
except ConnectionError as e:
    print(e)
