import os
from src.password_manager import PasswordManager

if __name__ == "__main__":
    pm = PasswordManager()
    sistem_os = os.name
    
    while(True):
        match sistem_os:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("SELAMAT DATANG DI MANAGER SANDI")
        print("SILAHKAN MASUKAN PIN ANDA")
        print("=========================")
        
        print("1. Tambah Password")
        print("2. Ambil Password")
        print("3. Hapus Password")
        print("0. Keluar")
        
        user_opsi = input("Masukan opsi : ")
        print("\n=========================\n")
        
        match user_opsi:
            case "1":
                service = input("Masukan Nama Layanan : ")
                username = input("Masukan username: ")
                password = input("Masukan password: ")
                pm.add_password(service, username, password)
            case "2": 
                service = input("Masukan nama layanan: ")
                username = input("Masukan username: ")
                pm.get_password(service, username)
            case "3": 
                service = input("Masukan nama layanan: ")
                username = input("Masukan username: ")
                pm.delete_password(service, username)
            case "0":
                 print("Anda Sudah Keluar, SIlahkan Masukan PIN Anda Kembali")
                 break
            
        print("\n=========================\n")
        is_done = input("Apakah Selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    print("Anda Sudah Keluar, SIlahkan Masukan PIN Anda Kembali")
