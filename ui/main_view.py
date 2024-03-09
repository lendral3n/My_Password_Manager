import os
from .password_management_view import PasswordManagementView
from .activity_log_view import ActivityLogView
class MainView:
    def __init__(self,  authentication, password_manager, activity_log):
        self.pm = password_manager  # Gunakan instance dari PasswordManager
        self.auth = authentication
        self.al = activity_log
        self.sistem_os = os.name
        
    def clear_screen(self):
        if self.sistem_os == "posix": 
            os.system("clear")
        elif self.sistem_os == "nt": 
            os.system("cls")
                
    def run(self):
        self.clear_screen()
        print("SELAMAT DATANG DI MANAGER SANDI")
        print("=========================")
        while True:
            
            if not self.auth.is_registered():
                print("1. Register PIN")
                print("2. Register Sandi")
                user_opsi = input("Masukan opsi : ")
                if user_opsi == "1":
                    pin = input("Masukkan PIN Anda: ")
                    self.auth.register("pin", pin)
                elif user_opsi == "2": 
                    sandi = input("Masukkan Sandi Anda: ")
                    self.auth.register("sandi", sandi)
            else:
                auth = input("Masukkan PIN Atau Sandi Anda: ")
                if auth.isdigit():
                    if not self.auth.authenticate(auth):
                        print("PIN Anda Salah")
                        print()
                        continue
                else:
                    if not self.auth.authenticate(auth):
                        print("Sandi Anda Salah")
                        print()
                        continue

                print("=========================")
                print("1. Kelola Password")
                print("2. Lihat Log Aktivitas")
                print("0. Keluar")
                
                user_opsi = input("Masukan opsi : ")
                print("\n=========================\n")
                
                if user_opsi == "1":
                    pmv = PasswordManagementView(self.pm)
                    pmv.run()
                elif user_opsi == "2": 
                    alv = ActivityLogView(self.al)
                    alv.run()
                elif user_opsi == "0":
                    print("Anda Sudah Keluar, SIlahkan Masukan PIN Anda Kembali")
                    break
                
                print("\n=========================\n")
                is_done = input("Apakah Selesai (y/n)? ")
                if is_done == "y" or is_done == "Y":
                    break
