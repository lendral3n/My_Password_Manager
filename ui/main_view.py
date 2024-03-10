import os
from .password_management_view import PasswordManagementView
from .activity_log_view import ActivityLogView
class MainView:
    def __init__(self,  authentication, password_manager, activity_log):
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
        self.clear_screen()
        print()
        print("""
                                                                                  
                                                       r#@@@@@@@@@#r           
                                                       ?@@@#x_`_v#@@@x          
                                                       g@@@!     !@@@Q          
                                                       Q@@@_     _@@@B          
                                                    rgg@@@@       @@@@ggr       
                                                    Y@@@@@@@@@@@@@@@@@@@Y       
                                                    Y@@@@@@@Qx^xQ@@@@@@@Y       
                                                    Y@@@@@@@^   ~@@@@@@@Y       
                                                    Y@@@@@@@@r r#@@@@@@@Y       
                                                    Y@@@@@@@@c,c@@@@@@@@Y       
                                                    Y@@@@@@@@@@@@@@@@@@@Y       
                                                    v###################v       
                                                    
                                                SELAMAT DATANG DI MANAGER SANDI
                                       """)
        print()            
        print("=========================")
        while True:
            if not self.auth.is_registered():
                print("1. Register PIN")
                print("2. Register Sandi")
                user_opsi = input("Masukan opsi : ")
                if user_opsi == "1":
                    pin = input("Masukkan PIN Anda: ")
                    self.auth.register("pin", pin)
                    activity = f"Pengguna Membuat PIN"
                    self.al.log_activity(activity)
                elif user_opsi == "2": 
                    sandi = input("Masukkan Sandi Anda: ")
                    self.auth.register("sandi", sandi)
                    activity = f"Pengguna Membuat Sandi"
                    self.al.log_activity(activity)
            else:
                print()
                auth = input("Masukkan PIN Atau Sandi Anda: ")
                if auth.isdigit():
                    if not self.auth.authenticate(auth):
                        print("PIN Anda Salah")
                        activity = f"Pengguna gagal masuk menggunakan PIN"
                        self.al.log_activity(activity)
                        print()
                        continue
                    else:
                        activity = f"Pengguna berhasil masuk menggunakan PIN"
                        self.al.log_activity(activity)
                else:
                    if not self.auth.authenticate(auth):
                        print("Sandi Anda Salah")
                        activity = f"Pengguna gagal masuk menggunakan Sandi"
                        self.al.log_activity(activity)
                        print()
                        continue
                    else:
                        activity = f"Pengguna berhasil masuk menggunakan Sandi"
                        self.al.log_activity(activity)

                print("=========================")
                print("1. Kelola Password")
                print("2. Lihat Log Aktivitas")
                print("0. Keluar")
                
                user_opsi = input("Masukan opsi : ")
                print("\n=========================\n")
                
                if user_opsi == "1":
                    pmv = PasswordManagementView(self.pm, self.auth, self.al)
                    if pmv.run() == True:
                        break
                elif user_opsi == "2": 
                    alv = ActivityLogView(self.auth, self.al)
                    if alv.run() == True:
                        break
                elif user_opsi == "0":
                    activity = f"Pengguna Keluar"
                    self.al.log_activity(activity)
                    print("Anda Sudah Keluar")
                    break
                
                print("\n=========================\n")
                is_done = input("Apakah Selesai (y/n)? ")
                if is_done == "y" or is_done == "Y":
                    break