import sqlite3
import conexion as conn


db = conn.DB()

id = '5385741366'
firstname = 'mario334'
username = 'mario2245'
referred_by = '2345'
invite_link = f'https://t.me/stainedpruebabot?start={id}'
rank = 'none'
wallet = 'none'
referrals = 0
status = 0

queryInsertUser = f'INSERT INTO user(id, firstname, username, referred_by, invite_link) \
    VALUES (?, ?, ?, ?, ?)'

parameters = (id, firstname, username, referred_by, invite_link)
try:
    db.execute_query(queryInsertUser, parameters)
except:
    print('usuario en existencia')

date = '2022/08/13'
user_id = id
queryInsertInvestment = f'INSERT INTO investments(date, user_id) VALUES (?, ?)'
parameters = (date, user_id)

try:
    db.execute_query(queryInsertInvestment, parameters)
except ConnectionError as e:
    print(e)

