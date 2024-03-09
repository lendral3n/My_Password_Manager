import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("./db/database.db")
        self.cursor = self.conn.cursor()

    def add_password(self, service, username, password):
        self.cursor.execute("INSERT INTO passwords VALUES (?, ?, ?)", (service, username, password))
        self.conn.commit()

    def get_password(self, service, username):
        self.cursor.execute("SELECT password FROM passwords WHERE service=? AND username=?", (service, username))
        return self.cursor.fetchone()

    def delete_password(self, service, username):
        self.cursor.execute("DELETE FROM passwords WHERE service=? AND username=?", (service, username))
        self.conn.commit()
