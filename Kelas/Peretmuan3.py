angka = 6
if angka < 10: 
    print("Angka kurang dari 10")


umur = int(input("Masukkan umur: ")) 

if umur >= 17:
    print("Kamu sudah bisa membuat KTP") 
else:
    print("Kamu belum bisa membuat KTP")


kendaraan = input("Masukkan jenis kendaraan anda: ")
if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000

    print("Tarif parkir yang harus dibayar:", tarif_parkir)

nilai = int(input("masukkan nilai :"))
if nilai > 90:
    print("A")
elif nilai > 80:
    print("B")
elif nilai >= 70:
    print("c")
elif nilai > 50 and nilai < 69:
    print("D")
else :
    print("D")


umur = 20
if umur >= 18:
    status = "Dewasa"
else:
    status = "Belum Dewasa"

umur = 20
status = "Dewasa" if umur >= 18 else "Belum Dewasa"