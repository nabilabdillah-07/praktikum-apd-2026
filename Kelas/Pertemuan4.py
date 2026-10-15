# batas = 5 
# for i in range(batas):
#     print("perulangan ke :", i)

# game = ["Genshin", 7.0, True]
# for i in game:
#     print(i)

# for i in range(1, 3):
#     for j in range(1, 4):
#      print(f'{i} x {j} = {i * j}')
#     print('')

# n = int(input("masukin bilangan n :"))
# jumlah = 0

# for i in range(1, n + 1):
#     if i % 2 == 1 :
#         jumlah = jumlah + 1

# print(f"jumlah bilangan ganjil di {n} adalah : {jumlah}")



# jawab = "ya"
# hitung = 0
# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total Perulangan : {hitung}")


# for i in range(10):
#     if i == 5:
#         break
#     print(i)


# angkaBenar = 7

# while True:
#     print("=== game tebak angka ===")

#     angkaInput = int(input("masukin angka 1-10 :"))

#     if angkaBenar == angkaInput:
#         print("angkanya benar")
#         break
#     else:
#         print("salah bego")


# for i in range(10):
#     if i % 2 == 0:
#         print(i)

saldo = int(input("masukin saku awal :"))

while saldo > 0:
    pengeluaran = int(input("masukin pengeluaran :"))

    if pengeluaran > saldo:
        print("saldo gk cukup")
        break
    else:
        saldo = saldo - pengeluaran
        print("saldo sekarang :", saldo)

print("saldo akhir :", saldo)
