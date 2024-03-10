# File: src/activity_log.py
from db.database import Database

class ActivityLog:
    def __init__(self):
        self.db = Database()

    def log_activity(self, activity):
        self.db.add_activity(activity)

    def get_activities(self):
        activities = self.db.get_activities()
        if activities:
            for activity in activities:
                print()
                print(f"Aktivitas ==> {activity[1]}")
                print(f"Waktu ==> {activity[2]}")
                print("\n=========================\n")
        else:
            print("Tidak ada aktivitas yang dicatat.")
