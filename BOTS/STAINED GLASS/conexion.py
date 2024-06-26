import sqlite3

database = 'users.db'

class DB:
    def execute_query(self, query, parameters=()):
        with sqlite3.connect(database) as conn:
            self.cursor = conn.cursor()
            result = self.cursor.execute(query, parameters)
            conn.commit()
            return result