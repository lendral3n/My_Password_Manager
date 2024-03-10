# File: db/database.py
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

    def get_password(self, service):
        self.cursor.execute("SELECT * FROM passwords WHERE service=?", (service,))
        return self.cursor.fetchone()

    def get_all_passwords(self):
        self.cursor.execute("SELECT * FROM passwords")
        return self.cursor.fetchall() 

    def delete_password(self, service):
        self.cursor.execute("DELETE FROM passwords WHERE service=?", (service,))
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

    def add_activity(self, activity):
        self.cursor.execute("""
            INSERT INTO activity_log (action)
            VALUES (?)
        """, (activity,))
        self.conn.commit()

    def get_activities(self):
        self.cursor.execute("SELECT * FROM activity_log")
        return self.cursor.fetchall()