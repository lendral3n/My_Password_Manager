from db.database import Database

class Authentication:
    def __init__(self):
        self.db = Database()

    def is_registered (self):
        return self.db.get_pin() is not None or self.db.get_sandi() is not None
    
    def register(self, method, value):
        if method == "pin":
            self.db.add_pin(value)
        elif method == "sandi":
            self.db.add_sandi(value)
            
    def authenticate(self, value):
        if value.isdigit():
            if self.db.get_pin()[0] != value:
                print()
                return False
        else:
            if self.db.get_sandi()[0] != value:
                print()
                return False
        return True
