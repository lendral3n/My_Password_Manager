# File: ui/activity_log_view.py
import os
class ActivityLogView:
    def __init__(self, authentication, activity_log):
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
            print("1. Lihat Riwayat Aktivitas")
            print("9. Kembali")
            
            user_opsi = input("Masukan opsi : ")
            print("\n=========================\n")
            
            if user_opsi == "1":
                self.al.get_activities()
            elif user_opsi == "9":
                self.clear_screen()
                return True
