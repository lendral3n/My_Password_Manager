from db.database import Database

class PasswordManager():
    def __init__(self):
        self.dbs = Database()

    def add_password(self, service, username, password, url, notes):
        self.dbs.add_password(service, username, password, url, notes)
        print(f"Password untuk {service} dan username {username} telah ditambahkan")
        
    def get_password(self, service, username):
        password = self.dbs.get_password(service, username)
        if password:
            print(f"Password untuk {service} dan username {username} adalah {password[0]}")
        else:
            print(f"Tidak ada password yang ditemukan untuk {service} dan username {username}")

    def delete_password(self, service, username):
        self.dbs.delete_password(service, username)
        print(f"Password untuk {service} dan username {username} telah dihapus.")