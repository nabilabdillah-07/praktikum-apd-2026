from auth import login, register
from crud import tambahData, ubahData, hapusData
from tampilan import pilihMenuAwal, pilihMenuUtama, tampilkanData
from utils import bersihkanLayar, jeda


def menuSetelahLogin(username, role):
    while True:
        bersihkanLayar()
        pilihan = pilihMenuUtama(role, username)

        if pilihan == "tambah":
            tambahData()
        elif pilihan == "lihat":
            tampilkanData()
        elif pilihan == "ubah":
            ubahData()
        elif pilihan == "hapus":
            hapusData()
        else:
            break

        jeda()


def main():
    while True:
        bersihkanLayar()
        pilihan = pilihMenuAwal()

        if pilihan == "login":
            hasil = login()
            if hasil is not None:
                username, role = hasil
                menuSetelahLogin(username, role)
        elif pilihan == "register":
            register()
        else:
            print("Program beres")
            break


main()
