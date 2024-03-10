# File: ui/password_management_view.py
import os
class PasswordManagementView:
    def __init__(self, password_manager, authentication, activity_log):
        self.pm = password_manager
        self.auth = authentication
        self.al = activity_log  
        self.sistem_os = os.name
        
    def clear_screen(self):
        if self.sistem_os == "posix": 
            os.system("clear")
        elif self.sistem_os == "nt": 
            os.system("cls")
               
    def run(self):
        while True:
            print("=========================")
            print("1. Tambah Password")
            print("2. Lihat Password")
            print("3. Hapus Password")
            print("9. Kembali")
            
            print()
            user_opsi = input("Masukan opsi : ")
            print("\n=========================\n")
            
            if user_opsi == "1":
                service = input("Masukkan nama layanan: ")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                url = input("Masukkan URL (jika ada): ")
                notes = input("Masukkan catatan (jika ada): ")
                self.pm.add_password(service, username, password, url, notes)
                activity = f"Pengguna menambahkan password baru untuk layanan {service}"
                self.al.log_activity(activity)
            elif user_opsi == "2": 
                auth = input("Masukkan PIN Atau Sandi Anda: ")
                if auth.isdigit():
                    if not self.auth.authenticate(auth):
                        print("PIN Anda Salah")
                        print()
                        activity = f"Pengguna gagal melihat password menggunakan PIN"
                        self.al.log_activity(activity)
                        return
                else:
                    if not self.auth.authenticate(auth):
                        print("Sandi Anda Salah")
                        print()
                        activity = f"Pengguna gagal melihat password menggunakan Sandi"
                        self.al.log_activity(activity)
                        return
                self.pm.get_all_passwords()
                activity = f"Pengguna melihat semua password"
                self.al.log_activity(activity)
                while True:
                    print()
                    print(" ==> Detail Password (Masukkan nama layanan)")
                    print(" ==> 9. Kembali")
                    print()
                    service = input("Pilih Opsi : ")
                    if service == "9":
                        self.clear_screen()
                        break
                    else:
                        self.pm.get_password(service)
                        activity = f"Pengguna melihat detail password untuk layanan {service}"
                        self.al.log_activity(activity)
                    print()
                    input("9. Kembali: ")
                    self.clear_screen()
                    break
            elif user_opsi == "3": 
                service = input("Masukkan nama layanan: ")
                print()
                auth = input("Masukkan PIN Atau Sandi Anda: ")
                if auth.isdigit():
                    if not self.auth.authenticate(auth):
                        print("PIN Anda Salah")
                        print()
                        activity = f"Pengguna gagal menghapus password menggunakan PIN"
                        self.al.log_activity(activity)
                        return
                else:
                    if not self.auth.authenticate(auth):
                        print("Sandi Anda Salah")
                        print()
                        activity = f"Pengguna gagal menghapus password menggunakan Sandi"
                        self.al.log_activity(activity)
                        return
                self.pm.delete_password(service)
                activity = f"Pengguna Berhasil menghapus password"
                self.al.log_activity(activity)
                while True:
                    print()
                    input("9. Kembali: ")
                    self.clear_screen()
                    break
            elif user_opsi == "9":
                self.clear_screen()
                return True
