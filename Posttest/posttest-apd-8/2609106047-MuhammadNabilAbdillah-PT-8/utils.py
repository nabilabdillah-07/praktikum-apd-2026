# File ini isinya fungsi bantu (input, hitung, dll)
import os
import inquirer


def bersihkanLayar():
    os.system("cls" if os.name == "nt" else "clear")


def jeda():
    input("\nPencet enter buat lanjut")


def hitungProfit(hargaBeli, hargaJual):
    return hargaJual - hargaBeli


def totalRekursif(daftarProfit, index):
    if index == len(daftarProfit):
        return 0
    else:
        return daftarProfit[index] + totalRekursif(daftarProfit, index + 1)


def inputTeks(pesan):
    jawaban = inquirer.prompt([inquirer.Text("isi", message=pesan)])
    if jawaban is None:  # kalau user pencet Ctrl+C
        return ""
    return jawaban["isi"].strip()


def inputPassword(pesan):
    jawaban = inquirer.prompt([inquirer.Password("isi", message=pesan)])
    if jawaban is None:
        return ""
    return jawaban["isi"]


def inputHarga(pesan):
    try:
        harga = int(inputTeks(pesan))
        if harga < 0:
            raise ValueError("Harganya jangan minus")
    except ValueError:
        print("Harganya harus angka terus jangan minus, coba lagi")
        return inputHarga(pesan)
    else:
        return harga


def pilihDariList(pesan, pilihan):
    # pilihan = list of (tulisan, nilai). Return None kalau dibatalin
    jawaban = inquirer.prompt([inquirer.List("pilih", message=pesan, choices=pilihan)])
    if jawaban is None:
        return None
    return jawaban["pilih"]


def konfirmasi(pesan):
    jawaban = inquirer.prompt([inquirer.Confirm("ya", message=pesan, default=False)])
    if jawaban is None:
        return False
    return jawaban["ya"]
