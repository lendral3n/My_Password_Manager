from cryptography.fernet import Fernet
from db.database import Database

class Encrypt:
    def __init__(self):
        self.key = Fernet.generate_key()

    # Fungsi untuk enkripsi
    def encrypt_message(self, message):
        f = Fernet(self.key)
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message

    # Fungsi untuk dekripsi
    def decrypt_message(self, encrypted_message):
        f = Fernet(self.key)
        decrypted_message = f.decrypt(encrypted_message).decode()
        return decrypted_message
