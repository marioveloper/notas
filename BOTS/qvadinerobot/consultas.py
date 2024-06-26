import conexion as conn
db = conn.DB()

result = db.execute_query('CREATE TABLE usuario')
print(result.fetchall())

def insert_query(context = []):
    result = db.execute_query()