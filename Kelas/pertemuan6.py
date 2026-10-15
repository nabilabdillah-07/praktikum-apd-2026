# kartu = {"merah", "merah", "biru", "hijau"}
# print(kartu)

# matkul = ["apd", "orsikom", "apd", "kalkulus"]
# sks = set(matkul)
# print(sks)


# buah = set(("apel", "jeruk", "mangga", "apel"))
# print(buah)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print (angka)

# kelas = {"a", "b", "c"}
# kelas.add("d")
# print(kelas)

# buah = {"apel", "mangga", "jeruk"}
# buah.remove("mangga")
# print(buah)


# aslab1 = {1,2,3,4,5}
# aslab2 = {2,4,6,8,10}
# selisih = aslab1.difference(aslab2)
# print(selisih)


# Matkul = {
#     "Matkul_ganjil" : "kalkulus",
#     "Matkul_genap" : "statistik"
# }

# print(Matkul["Matkul_genap"])
# print(Matkul)


# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }

# print(f"nama saya adalah {Biodata['Nama']}")




# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }

# print(f"Nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat"))
# print(Biodata.get("Alamat", "Key untuk alamat tidak ada"))





# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }

# print(game)
# game["genshin impact"] = "adventure"
# print(game)











# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }


# print("Panjang dictionary :", len(aset))
# print(len(aset))



menu = {
"ayam geprek" : 15000,
"ayam goreng" : 13000,
"ayam bakar" : 17000,
"nasi goreng" : 12000,
"mie goreng" : 10000
}
menu_baru = menu.copy()
menu_baru["nasi goreng"] = 15000
print(menu)
print(menu_baru)