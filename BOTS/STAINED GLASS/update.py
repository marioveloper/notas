import conexion as conn

db = conn.DB()

wallet = ''
user_id = '4534'
queryUpdateWallet = f'UPDATE user SET wallet = ? WHERE id = ?'
parameters = (wallet, user_id)

try:
    db.execute_query(queryUpdateWallet, parameters)
except ConnectionError as e:
    print(e)
