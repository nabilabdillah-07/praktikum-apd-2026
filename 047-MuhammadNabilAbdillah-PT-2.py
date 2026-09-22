makanan_1 = 15000
makanan_2 = 16000
makanan_3 = 19000
makanan_4 = 20000
makanan_5 = 21000
makanan_6 = 22000
hargaMakanan = [makanan_1, makanan_2, makanan_3, makanan_4, makanan_5, makanan_6]

biayaAplikasi = 5000
total_bayar = makanan_1 + makanan_2 + makanan_3 + makanan_4 + makanan_5 + makanan_6
rata_rata = total_bayar / len(hargaMakanan)

nim = 47
bolean = nim != rata_rata

kursEuro = 20500
totalBayarEuro = total_bayar / kursEuro

print("Total bayar :", total_bayar)
print("Rata rata :", rata_rata)
print("NIM :", nim)
print("Hasil bolean :", bolean)
print("Totaal bayar euro :", totalBayarEuro)
print("Harga makanan :", hargaMakanan[-6:])