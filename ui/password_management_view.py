# File: ui/password_management_view.py

class PasswordManagementView:
    def __init__(self, password_manager):
        self.pm = password_manager

    def run(self):
        print("=========================")
        print("1. Tambah Password")
        print("2. Ambil Password")
        print("3. Hapus Password")
        print("0. Kembali")
        
        user_opsi = input("Masukan opsi : ")
        print("\n=========================\n")
        
        if user_opsi == "1":
            service = input("Masukkan nama layanan: ")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            url = input("Masukkan URL (jika ada): ")
            notes = input("Masukkan catatan (jika ada): ")
            self.pm.add_password(service, username, password, url, notes)
        elif user_opsi == "2": 
            service = input("Masukkan nama layanan: ")
            self.pm.get_password(service)
        elif user_opsi == "3": 
            service = input("Masukkan nama layanan: ")
            self.pm.delete_password(service)
        elif user_opsi == "0":
            return
