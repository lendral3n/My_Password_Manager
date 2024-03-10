from src.password_manager import PasswordManager
from src.authentication import Authentication
from src.activity_log import ActivityLog
from db.create_table import create_tables
from ui.main_view import MainView
from ui.password_management_view import PasswordManagementView
from ui.activity_log_view import ActivityLogView

if __name__ == "__main__":
    pm = PasswordManager()
    auth = Authentication()
    log = ActivityLog()
    db = create_tables()
    pmview = PasswordManagementView(pm, auth, log)
    logview = ActivityLogView(auth, log)
    mv = MainView(auth, pm, log)
    mv.run()
