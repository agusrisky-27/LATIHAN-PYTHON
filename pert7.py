# # # =========================
# # # HITUNG GAJI
# # # =========================

# # # Nama : Risky

# # # Gaji Pokok : 5000000

# # # Bonus : 1000000

# # # Total Gaji : 6000000

# # def garis():
# #     print ("====================")

# # garis()
# # print ("SELAMAT DATANG")
# # garis()

# # nama = input("Masukan Nama Anda : ",)
# # umur = int(input("Masukan Umur Anda : "))
# # alamat = input("Masukan aamat anda : ")

# # garis()
# # print ("BIODATA")
# # garis()

# # print ("Nama : ", nama)
# # print ("Umur : ", umur)
# # print ("Alamat : ", alamat)

# SOAL 17
# =========================
#     DATA PEGAWAI
# =========================

# 1. Tambah Data
# 2. Tampilkan Data
# 3. Cek Gaji
# 4. Keluar

# Pilih : 1

# Nama : Risky
# NIP : 240040110
# Gaji : 6000000

# Data berhasil ditambahkan

# Pilih : 2

# =========================
# DATA PEGAWAI
# =========================

# Nama : Risky
# NIP : 240040110
# Gaji : 6000000

# Pilih : 3

# Gaji : 6000000
# Status : Gaji Tinggi

# Pilih : 4

# Program selesai

print("=========================")
print("    DATA PEGAWAI")
print("=========================")

nama = ""
nip = ""
gaji = 0


def tambah_data():

    global nama
    global nip
    global gaji

    nama = input("Masukan Nama : ")
    nip = input("Masukan NIP : ")
    gaji = int(input("Masukan Gaji : "))

    print("Data berhasil ditambahkan")


def tampil_data():

    print("=========================")
    print("DATA PEGAWAI")
    print("=========================")

    print("Nama :", nama)
    print("NIP :", nip)
    print("Gaji :", gaji)


def cek_gaji():

    if gaji >= 5000000:
        return "Gaji Tinggi"

    else:
        return "Gaji Rendah"


def menu():

    print("\n1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Cek Gaji")
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

        hasil = cek_gaji()

        print("Gaji :", gaji)
        print("Status :", hasil)

    elif pilihan == "4":

        print("Program selesai")

        jalan = False

    else:

        print("Menu tidak tersedia")