import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("./db/database.db")
        self.cursor = self.conn.cursor()

    def add_password(self, service, username, password, url, notes):
        self.cursor.execute("""
            INSERT INTO passwords (service, username, password, url, notes)
            VALUES (?, ?, ?, ?, ?)
        """, (service, username, password, url, notes))
        self.conn.commit()

    def get_password(self, service, username):
        self.cursor.execute("SELECT password FROM passwords WHERE service=? AND username=?", (service, username))
        return self.cursor.fetchone()

    def delete_password(self, service, username):
        self.cursor.execute("DELETE FROM passwords WHERE service=? AND username=?", (service, username))
        self.conn.commit()
    
    def add_sandi(self, sandi):
        self.cursor.execute("INSERT INTO users (sandi) VALUES (?)", (sandi,))
        self.conn.commit()
    
    def add_pin(self, pin):
        self.cursor.execute("INSERT INTO users (pin) VALUES (?)", (pin,))
        self.conn.commit()
    
    def get_sandi(self):
        self.cursor.execute("SELECT sandi FROM users")
        return self.cursor.fetchone()
    
    def get_pin(self):
        self.cursor.execute("SELECT pin FROM users")
        return self.cursor.fetchone()
        
