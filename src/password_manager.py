from db.database import Database
from .encryption import Encrypt
class PasswordManager():
    def __init__(self):
        self.dbs = Database()
        self.encryptor = Encrypt() 

    def add_password(self, service, username, password, url, notes):
        encrypted_password = self.encryptor.encrypt_message(password) 
        self.dbs.add_password(service, username, encrypted_password, url, notes)
        print(f"Password untuk {service} dan username {username} telah ditambahkan")
        
    def get_password(self, service, username):
        encrypted_password = self.dbs.get_password(service, username)
        if encrypted_password:
            password = self.encryptor.decrypt_message(encrypted_password[0])
            print(f"Password untuk {service} dan username {username} adalah {password}")
        else:
            print(f"Tidak ada password yang ditemukan untuk {service} dan username {username}")

    def delete_password(self, service, username):
        self.dbs.delete_password(service, username)
        print(f"Password untuk {service} dan username {username} telah dihapus.")