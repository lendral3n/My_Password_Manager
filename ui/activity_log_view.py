# File: ui/activity_log_view.py

class ActivityLogView:
    def __init__(self, activity_log):
        self.al = activity_log

    def run(self):
        print("=========================")
        print("1. Lihat Log Aktivitas")
        print("0. Kembali")
        
        user_opsi = input("Masukan opsi : ")
        print("\n=========================\n")
        
        if user_opsi == "1":
            logs = self.al.get_logs()
            for log in logs:
                print(log)
        elif user_opsi == "0":
            return
