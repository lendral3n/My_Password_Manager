from cryptography.fernet import Fernet

class KeyGenerator:
    @staticmethod
    def generate_key():
        try:
            with open("./db/key.key", "rb") as key_file:
                key = key_file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open("./db/key.key", "wb") as key_file:
                key_file.write(key)
        return key

class Encrypt:
    def __init__(self):
        self.key = KeyGenerator.generate_key()

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
