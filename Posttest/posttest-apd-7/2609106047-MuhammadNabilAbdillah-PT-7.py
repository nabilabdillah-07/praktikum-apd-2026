import os

dataUser = {
    "admin": {"password": "admin123", "role": "admin"},
    "nabil": {"password": "047", "role": "user"}
}

dataPenjualan = {
    1: {"item": "Borealis", "hargaBeli": 32000, "hargaJual": 41000, "profit": 9000},
    2: {"item": "Jack nf", "hargaBeli": 16800, "hargaJual": 17500, "profit": 700}
}
idBerikutnya = 3

def cekDataKosong():
    return len(dataPenjualan) == 0


def hitungTotalProfit():
    daftarProfit = []
    for data in dataPenjualan.values():
        daftarProfit.append(data["profit"])
    return totalRekursif(daftarProfit, 0)

def hitungProfit(hargaBeli, hargaJual):
    return hargaJual - hargaBeli

def totalRekursif(daftarProfit, index):
    if index == len(daftarProfit):
        return 0
    else:
        return daftarProfit[index] + totalRekursif(daftarProfit, index + 1)

def inputHarga(pesan):
    try:
        harga = int(input(pesan))
        if harga < 0:
            raise ValueError("Harganya jangan minus")
    except ValueError:
        print("Harganya harus angka terus jangan minus, coba lagi")
        return inputHarga(pesan)
    else:
        return harga

def tampilkanMenu(role, username):
    print("=== MENU", role.upper(), "-", username, "===")
    if role == "admin":
        print("1. Tambah data")
    print("2. Lihat data")
    if role == "admin":
        print("3. Ubah data")
        print("4. Hapus data")
    print("5. Logout")


def tampilkanData():
    if cekDataKosong():
        print("Datanya masih kosong")
    else:
        print("No | Item | Beli | Jual | Profit")
        for nomorData, data in dataPenjualan.items():
            print(nomorData, "|", data["item"], "|", data["hargaBeli"], "|", data["hargaJual"], "|", data["profit"])
        totalProfit = hitungTotalProfit()
        print("Total profit:", totalProfit)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("--- PROFIT ITEM BLADE BALL ---")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Mau pilih yang mana? : ")

    if pilih == "1":
        username = input("Username: ")
        password = input("Password: ")

        role = ""
        if username in dataUser and dataUser[username]["password"] == password:
            role = dataUser[username]["role"]

        if role == "":
            print("Username atau password nya salah")
            input("Pencet enter buat lanjut")
            continue

        while True:
            os.system("cls" if os.name == "nt" else "clear")
            tampilkanMenu(role, username)
            menu = input("Pilih yang mana?")

            if role == "user" and menu in ["1", "3", "4"]:
                print("Menu nya cuma buat admin ya")
                input("Pencet enter buat lanjut")
                continue

            if menu == "1":
                try:
                    namaItem = input("Nama item: ")
                    if namaItem == "":
                        raise ValueError("Nama item nya jangan kosong dong")
                    hargaBeli = inputHarga("Harga beli: ")
                    hargaJual = inputHarga("Harga jual: ")
                except ValueError as e:
                    print(e)
                else:
                    dataPenjualan[idBerikutnya] = {"item": namaItem, "hargaBeli": hargaBeli, "hargaJual": hargaJual, "profit": hitungProfit(hargaBeli, hargaJual)}
                    idBerikutnya += 1
                    print("Oke, data udah ditambah")
                finally:
                    print("Proses tambah data selesai")

            elif menu in ["2", "3", "4"]:
                tampilkanData()

                if not cekDataKosong():
                    if menu == "3":
                        try:
                            nomorInput = input("Nomor data yang mau diubah: ")
                            if not nomorInput.isdigit():
                                raise ValueError("Nomornya harus angka ya")
                            nomor = int(nomorInput)
                            if nomor not in dataPenjualan:
                                raise KeyError(nomor)
                            namaItem = input("Nama item baru: ")
                            if namaItem == "":
                                raise ValueError("Nama item nya jangan kosong dong")
                            hargaBeli = inputHarga("Harga beli baru: ")
                            hargaJual = inputHarga("Harga jual baru: ")
                        except KeyError:
                            print("Nomornya nggak ada")
                        except ValueError as e:
                            print(e)
                        else:
                            dataPenjualan[nomor] = {"item": namaItem, "hargaBeli": hargaBeli, "hargaJual": hargaJual, "profit": hitungProfit(hargaBeli, hargaJual)}
                            print("Data udah diubah")
                        finally:
                            print("Proses ubah data selesai")

                    elif menu == "4":
                        try:
                            nomorInput = input("Nomor data yang mau dihapus: ")
                            if not nomorInput.isdigit():
                                raise ValueError("Nomornya harus angka ya")
                            nomor = int(nomorInput)
                            if nomor not in dataPenjualan:
                                raise KeyError(nomor)
                        except KeyError:
                            print("Nomornya gaada")
                        except ValueError as e:
                            print(e)
                        else:
                            del dataPenjualan[nomor]
                            print("Data dah dihapus")
                        finally:
                            print("Proses hapus data selesai")

            elif menu == "5":
                break

            else:
                print("Pilihannya gaada")

            input("\nPencet enter buat lanjut")

    elif pilih == "2":
        usernameBaru = input("Username baru: ")
        passwordBaru = input("Password baru: ")

        try:
            if usernameBaru == "" or passwordBaru == "":
                raise ValueError("Username sama passwordnya gaboleh kosong yh")
            if usernameBaru in dataUser:
                raise ValueError("Username nya udah dipake, cari yang lain")
        except ValueError as e:
            print(e)
        else:
            dataUser[usernameBaru] = {"password": passwordBaru, "role": "user"}
            print("Register berhasil, sekarang bisa login")
        finally:
            input("Pencet enter buat lanjut")

    elif pilih == "3":
        print("Program beres")
        break

    else:
        print("Pilihannya gaada")
        input("Pencet enter buat lanjut")