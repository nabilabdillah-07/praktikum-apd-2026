# File ini isinya semua yang berhubungan sama tampilan (prettytable + menu)
from prettytable import PrettyTable
from data import dataPenjualan
from utils import totalRekursif, pilihDariList


def cekDataKosong():
    return len(dataPenjualan) == 0


def hitungTotalProfit():
    daftarProfit = []
    for data in dataPenjualan.values():
        daftarProfit.append(data["profit"])
    return totalRekursif(daftarProfit, 0)


def tampilkanJudul(teks):
    tabel = PrettyTable()
    tabel.field_names = [teks]
    print(tabel)


def tampilkanData():
    if cekDataKosong():
        print("Datanya masih kosong")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Item", "Harga Beli", "Harga Jual", "Profit"]
    tabel.align["Item"] = "l"
    for nomor, data in dataPenjualan.items():
        tabel.add_row([nomor, data["item"], data["hargaBeli"], data["hargaJual"], data["profit"]])
    print(tabel)
    print("Total profit:", hitungTotalProfit())


def pilihMenuAwal():
    tampilkanJudul("PROFIT ITEM BLADE BALL")
    return pilihDariList("Mau pilih yang mana?", [
        ("Login", "login"),
        ("Register", "register"),
        ("Keluar", "keluar")
    ])


def pilihMenuUtama(role, username):
    tampilkanJudul("MENU " + role.upper() + " - " + username)
    pilihan = []
    if role == "admin":
        pilihan.append(("Tambah data", "tambah"))
    pilihan.append(("Lihat data", "lihat"))
    if role == "admin":
        pilihan.append(("Ubah data", "ubah"))
        pilihan.append(("Hapus data", "hapus"))
    pilihan.append(("Logout", "logout"))
    return pilihDariList("Pilih yang mana?", pilihan)
