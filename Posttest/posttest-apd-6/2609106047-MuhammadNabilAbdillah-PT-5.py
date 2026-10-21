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
            print("=== MENU", role.upper(), "-", username, "===")
            if role == "admin":
                print("1. Tambah data")
            print("2. Lihat data")
            if role == "admin":
                print("3. Ubah data")
                print("4. Hapus data")
            print("5. Logout")
            menu = input("Pilih yang mana?")

            if role == "user" and menu in ["1", "3", "4"]:
                print("Menu nya cuma buat admin ya")
                input("Pencet enter buat lanjut")
                continue

            if menu == "1":
                namaItem = input("Nama item: ")
                hargaBeli = input("Harga beli: ")
                hargaJual = input("Harga jual: ")
                if namaItem == "":
                    print("Nama item nya jangan kosong dong")
                elif not hargaBeli.isdigit() or not hargaJual.isdigit():
                    print("Harganya harus angka terus jangan minus")
                else:
                    hargaBeli = int(hargaBeli)
                    hargaJual = int(hargaJual)
                    dataPenjualan[idBerikutnya] = {"item": namaItem, "hargaBeli": hargaBeli, "hargaJual": hargaJual, "profit": hargaJual - hargaBeli}
                    idBerikutnya += 1
                    print("Oke, data udah ditambah")

            elif menu in ["2", "3", "4"]:
                if len(dataPenjualan) == 0:
                    print("Datanya masih kosong")
                else:
                    totalProfit = 0
                    print("No | Item | Beli | Jual | Profit")
                    for nomorData, data in dataPenjualan.items():
                        print(nomorData, "|", data["item"], "|", data["hargaBeli"], "|", data["hargaJual"], "|", data["profit"])
                        totalProfit += data["profit"]
                    print("Total profit:", totalProfit)

                    if menu == "3":
                        nomor = input("Nomor data yang mau diubah: ")
                        if not nomor.isdigit() or int(nomor) not in dataPenjualan:
                            print("Nomornya nggak ada")
                        else:
                            namaItem = input("Nama item baru: ")
                            hargaBeli = input("Harga beli baru: ")
                            hargaJual = input("Harga jual baru: ")
                            if namaItem == "":
                                print("Nama item nya jangan kosong dong")
                            elif not hargaBeli.isdigit() or not hargaJual.isdigit():
                                print("Harganya harus angka terus jangan minus")
                            else:
                                hargaBeli = int(hargaBeli)
                                hargaJual = int(hargaJual)
                                dataPenjualan[int(nomor)] = {"item": namaItem, "hargaBeli": hargaBeli, "hargaJual": hargaJual, "profit": hargaJual - hargaBeli}
                                print("Data udah diubah")

                    elif menu == "4":
                        nomor = input("Nomor data yang mau dihapus: ")
                        if not nomor.isdigit() or int(nomor) not in dataPenjualan:
                            print("Nomornya gaada")
                        else:
                            del dataPenjualan[int(nomor)]
                            print("Data dah dihapus")

            elif menu == "5":
                break

            else:
                print("Pilihannya gaada")

            input("\nPencet enter buat lanjut")

    elif pilih == "2":
        usernameBaru = input("Username baru: ")
        passwordBaru = input("Password baru: ")

        if usernameBaru == "" or passwordBaru == "":
            print("Username sama passwordnya gaboleh kosong yh")
        elif usernameBaru in dataUser:
            print("Username nya udah dipake, cari yang lain")
        else:
            dataUser[usernameBaru] = {"password": passwordBaru, "role": "user"}
            print("Register berhasil, sekarang bisa login")
        input("Pencet enter buat lanjut")

    elif pilih == "3":
        print("Program beres")
        break

    else:
        print("Pilihannya gaada")
        input("Pencet enter buat lanjut")