# =========================
#       DATA BARANG
# =========================

# 1. Tambah Barang
# 2. Tampilkan Barang
# 3. Cek Stok
# 4. Keluar

# Pilih : 1

# Nama Barang : Laptop
# Kode Barang : BR001
# Stok : 15

# Data berhasil ditambahkan

# Pilih : 2

# =========================
#      DATA BARANG
# =========================

# Nama Barang : Laptop
# Kode Barang : BR001
# Stok : 15

# Pilih : 3

# Stok : 15
# Status : Stok Aman

# Pilih : 4

# Program selesai

print("=========================")
print("      DATA BARANG")
print("=========================")

nama_barang = ""
kode_barang = ""
stok = 0


def tambah_data():

    global nama_barang
    global kode_barang
    global stok

    nama_barang = input("Nama Barang : ")
    kode_barang = input("Kode Barang : ")
    stok = int(input("Stok : "))

    print("Data berhasil ditambahkan")


def tampil_data():

    print("=========================")
    print("      DATA BARANG")
    print("=========================")

    print("Nama Barang :", nama_barang)
    print("Kode Barang :", kode_barang)
    print("Stok :", stok)


def cek_stok():

    if stok >= 10:
        return "Stok Aman"

    else:
        return "Stok Hampir Habis"


def menu():

    print("\n1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Cek Stok")
    print("4. Keluar")


jalan = True

while jalan:

    menu()

    pilihan = input("Pilih : ")

    if pilihan == "1":

        tambah_data()

    elif pilihan == "2":

        tampil_data()

    elif pilihan == "3":

        hasil = cek_stok()

        print("Stok :", stok)
        print("Status :", hasil)

    elif pilihan == "4":

        print("Program selesai")

        jalan = False

    else:

        print("Menu tidak tersedia")