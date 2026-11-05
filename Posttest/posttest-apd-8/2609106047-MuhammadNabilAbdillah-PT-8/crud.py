# File ini isinya fungsi tambah, ubah, hapus data
from data import dataPenjualan, state
from utils import inputTeks, inputHarga, hitungProfit, pilihDariList, konfirmasi
from tampilan import tampilkanData, cekDataKosong


def tambahData():
    try:
        namaItem = inputTeks("Nama item")
        if namaItem == "":
            raise ValueError("Nama item nya jangan kosong dong")
        hargaBeli = inputHarga("Harga beli")
        hargaJual = inputHarga("Harga jual")
    except ValueError as e:
        print(e)
    else:
        dataPenjualan[state["idBerikutnya"]] = {
            "item": namaItem,
            "hargaBeli": hargaBeli,
            "hargaJual": hargaJual,
            "profit": hitungProfit(hargaBeli, hargaJual)
        }
        state["idBerikutnya"] += 1
        print("Oke, data udah ditambah")
    finally:
        print("Proses tambah data selesai")


def pilihNomor(pesan):
    pilihan = []
    for nomor, data in dataPenjualan.items():
        pilihan.append((str(nomor) + " - " + data["item"], nomor))
    return pilihDariList(pesan, pilihan)


def ubahData():
    tampilkanData()
    if cekDataKosong():
        return

    try:
        nomor = pilihNomor("Pilih data yang mau diubah")
        if nomor is None:
            raise KeyError(nomor)
        namaItem = inputTeks("Nama item baru")
        if namaItem == "":
            raise ValueError("Nama item nya jangan kosong dong")
        hargaBeli = inputHarga("Harga beli baru")
        hargaJual = inputHarga("Harga jual baru")
    except KeyError:
        print("Ubah data dibatalin")
    except ValueError as e:
        print(e)
    else:
        dataPenjualan[nomor] = {
            "item": namaItem,
            "hargaBeli": hargaBeli,
            "hargaJual": hargaJual,
            "profit": hitungProfit(hargaBeli, hargaJual)
        }
        print("Data udah diubah")
    finally:
        print("Proses ubah data selesai")


def hapusData():
    tampilkanData()
    if cekDataKosong():
        return

    try:
        nomor = pilihNomor("Pilih data yang mau dihapus")
        if nomor is None:
            raise KeyError(nomor)
        if not konfirmasi("Yakin mau hapus " + dataPenjualan[nomor]["item"] + "?"):
            raise ValueError("Hapus data dibatalin")
    except KeyError:
        print("Hapus data dibatalin")
    except ValueError as e:
        print(e)
    else:
        del dataPenjualan[nomor]
        print("Data dah dihapus")
    finally:
        print("Proses hapus data selesai")
