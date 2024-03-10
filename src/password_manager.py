from db.database import Database
from .encryption import Encrypt

class PasswordManager():
    def __init__(self):
        self.dbs = Database()
        self.encryptor = Encrypt() 

    def add_password(self, service, username, password, url, notes):
        encrypted_password = self.encryptor.encrypt_message(password) 
        self.dbs.add_password(service, username, encrypted_password, url, notes)
        print()
        print(f"Password untuk {service} telah ditambahkan")
        
    def get_password(self, service):
        encrypted_password = self.dbs.get_password(service)
        if encrypted_password:
            password = self.encryptor.decrypt_message(encrypted_password[3])
            print()
            print(f"Layanan ==> {encrypted_password[1]}")
            print(f"Username ==> {encrypted_password[2]}")
            print(f"Password ==> {password}")
            print(f"URL ==> {encrypted_password[4]}")
            print(f"Catatan ==> {encrypted_password[5]}")
            print(f"Dibuat ==> {encrypted_password[6]}")
        else:
            print("Tidak ada password yang ditemukan.")
        
    def get_all_passwords(self):
        encrypted_passwords = self.dbs.get_all_passwords()
        if encrypted_passwords:
            for encrypted_password in encrypted_passwords:
                print()
                print(f"Layanan ==> {encrypted_password[1]}")
                print(f"Password ==> {encrypted_password[3]}")
                print("\n=========================\n")
        else:
            print()
            print("Tidak ada password yang disimpan.")

    def delete_password(self, service):
        self.dbs.delete_password(service)
        print()
        print(f"Password untuk {service} telah dihapus.")
