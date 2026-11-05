# File ini isinya login dan register
from data import dataUser
from utils import inputTeks, inputPassword, jeda


def login():
    username = inputTeks("Username")
    password = inputPassword("Password")

    if username in dataUser and dataUser[username]["password"] == password:
        return username, dataUser[username]["role"]

    print("Username atau password nya salah")
    jeda()
    return None


def register():
    usernameBaru = inputTeks("Username baru")
    passwordBaru = inputPassword("Password baru")

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
        jeda()
