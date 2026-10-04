usernameBenar = "nabil"     
passwordBenar = "047"

print("--- Login Sistem ---")

while True:
    username = input("Username : ")
    password = input("Password : ")

    if username == "" or password == "":
        print("Username dan password gaboleh kosong!")
        print("")
        continue

    if username.lower() == usernameBenar.lower() and password == passwordBenar:
        print("Login berhasil!!!")
        print("")
        break

    if username.lower() != usernameBenar.lower():
        print("Username salah!")
    if password != passwordBenar:
        print("Password salah!")
    print("Coba Lagi")
    print("")

totalKalimantanGambut = 0
totalKalimantanMineral = 0
totalSumateraGambut = 0
totalSumateraMineral = 0

while True:
    print("--- Input Titik Api ---")

    while True:
        pulau = input("Masukkan pulau (Kalimantan/Sumatera) : ").upper()
        if pulau == "":
            print("Input gaboleh kosong!")
            continue
        if pulau == "KALIMANTAN" or pulau == "SUMATERA":
            break
        print("Pilihan cuman ada Kalimantan atau Sumatera")

    if pulau == "KALIMANTAN":
        while True:
            lahan = input("Masukkan jenis lahan (Gambut/Mineral) : ").upper()
            if lahan == "":
                print("Input gaboleh kosong!")
                continue
            if lahan == "GAMBUT" or lahan == "MINERAL":
                break
            print("Pilihan cuman ada Gambut atau Mineral.")

        if lahan == "GAMBUT":
            kategori = "Kalimantan-Gambut"
        else:
            kategori = "Kalimantan-Mineral"
    else:
        while True:
            lahan = input("Masukkan jenis lahan (Gambut/Mineral) : ").upper()
            if lahan == "":
                print("Input tidak boleh kosong!")
                continue
            if lahan == "GAMBUT" or lahan == "MINERAL":
                break
            print("Jenis lahan tidak tersedia! Pilih Gambut atau Mineral.")

        if lahan == "GAMBUT":
            kategori = "Sumatera-Gambut"
        else:
            kategori = "Sumatera-Mineral"

    print("Kategori :", kategori)

    while True:
        hotspotInput = input("Jumlah titik api : ")
        if hotspotInput == "":
            print("Input gaboleh kosong!")
            continue
        break

    hotspot = int(hotspotInput)
    luas = hotspot * 5
    print("Luas lahan yang terbakar :", luas, "Hektare")

    if kategori == "Kalimantan-Gambut":
        totalKalimantanGambut += luas
    elif kategori == "Kalimantan-Mineral":
        totalKalimantanMineral += luas
    elif kategori == "Sumatera-Gambut":
        totalSumateraGambut += luas
    else:
        totalSumateraMineral += luas

    while True:
        jawab = input("Apakah masih mau input data titik api lagi? (Y/T) : ").upper()
        if jawab == "":
            print("Input gaboleh kosong!")
            continue
        if jawab == "Y" or jawab == "T":
            break
        print("Cuman boleh jwab Y/T")

    print("")

    if jawab == "T":
        break

totalSemua = (totalKalimantanGambut + totalKalimantanMineral
              + totalSumateraGambut + totalSumateraMineral)

print("Ringkasan Luas Lahan Yang Terbakar")
print("-------------------------------------------")
print("Kalimantan-Gambut  :", totalKalimantanGambut, "Hektare")
print("Kalimantan-Mineral :", totalKalimantanMineral, "Hektare")
print("Sumatera-Gambut    :", totalSumateraGambut, "Hektare")
print("Sumatera-Mineral   :", totalSumateraMineral, "Hektare")
print("-------------------------------------------")
print("Total keseluruhan  :", totalSemua, "Hektare")