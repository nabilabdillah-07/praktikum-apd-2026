namaAku = "Muhammad Nabil Abdillah"
nimAku  = "47"

biayaLangganan = 1500000

print("Welcome to ANGKASAAA")
inputNama = input("Masukkan Nama   : ")
inputNim  = input("Masukkan NIM    : ")

if inputNama.lower() == namaAku.lower() and inputNim == nimAku :
    print("\nLogin Berhasil!!! Welcome Yak,", inputNama)

    print("\nPilih Paket Yang Kamu Mau")
    print("1. Orbit       - admin (1%)")
    print("2. Nebula      - admin (3%)")
    print("3. Galaxy      - admin (5%)")
    print("4. SuperNova   - admin (7%)")

    paket = input("\nPilih Nomor Paket (1-4): ")

    if paket == "1":
        namaPaket = "Orbit"
        admin = 0.01
        persenAdmin = 1
        fitur = "Kamu cuman bisa dapat akses dasar ke lagu-lagu populer yh"
    elif paket == "2":
        namaPaket = "Nebula"
        admin = 0.03
        persenAdmin = 3
        fitur = "Kamu bisa denger lagu premium sama bikin playlist cuy"
    elif paket == "3":
        namaPaket = "Galaxy"
        admin = 0.05
        persenAdmin = 5
        fitur = "Sama kek galaxy tapi sekarang bisa offline jugak"
    elif paket == "4":
        namaPaket = "SuperNova"
        admin = 0.07
        persenAdmin = 7
        fitur = "Kamu dapat semua fitur dari paket-paket sebelumnya, dan juga dapat konten eksklusif artis-artis(km org have y)"
    else:
        paket = None

    if paket != None:
        biayaAdmin = round(biayaLangganan * admin)
        totalBayar = biayaLangganan + biayaAdmin

        print("Paket yang dipilih   : ", namaPaket)
        print("Harga Langganan      : Rp", biayaLangganan)
        print(f"Biaya admin ({persenAdmin})      : Rp", biayaAdmin)
        print("Total Bayar          : Rp", totalBayar)
        print("Fitur yang didapat   :", fitur)
    else:
        print("\nPaket yang kamu pilih gaada")

else:
    print("Login gagal, nama atau nim kamu ga sesuai")
    print("Program berhenti")