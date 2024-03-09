# File: src/activity_log.py
from db.database import Database

class ActivityLog:
    def __init__(self):
        self.db = Database()

    def log_activity(self, activity):
        # Simpan aktivitas ke database
        self.db.add_activity(activity)

    def get_logs(self):
        # Ambil log aktivitas dari database
        return self.db.get_activities()
