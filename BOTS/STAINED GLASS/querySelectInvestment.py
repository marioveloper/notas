import conexion as conn

db = conn.DB()

querySelectInvestment = 'SELECT * FROM investments'

try:
    table = db.execute_query(querySelectInvestment)
    filas = table.fetchall()
    for row in filas:
            print("ID: ", row[0])
            print("Date ", row[1])
            print("UserId", row[2])
except ConnectionError as e:
    print(e)