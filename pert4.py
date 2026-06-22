# # # # SOAL 11
# # # # =========================
# # # #       STATISTIK ANGKA
# # # # =========================

# # # # Masukkan jumlah angka : 6


# # # # Angka ke-1 : 10
# # # # Angka ke-2 : -5
# # # # Angka ke-3 : 0
# # # # Angka ke-4 : 20
# # # # Angka ke-5 : -3
# # # # Angka ke-6 : 8


# # # # =========================
# # # # HASIL
# # # # =========================

# # # # Jumlah Positif : 3
# # # # Jumlah Negatif : 2
# # # # Jumlah Nol     : 1

# # # # =========================

# # # print ("=========================")
# # # print ("     STATISTIK ANGKA     ")
# # # print ("=========================")

# # # positif = 0
# # # negatif = 0
# # # nol = 0 

# # # jumlah_angka = int(input("Masukan Jumlah Angka : "))
# # # for i in range(jumlah_angka):
# # #     angka = int(input("Masukan angka : "))

# # #     if angka > 0:
# # #         positif = positif + 1
# # #     elif angka < 0:
# # #         negatif = negatif + 1
# # #     else:
# # #         nol = nol + 1


# # # print ("=========================")
# # # print ("          HASIL          ")
# # # print ("=========================")
# # # print ("\nJumlah Positif : ", positif)
# # # print ("Jumlah Negatif : ", negatif)
# # # print ("Jumlah Nol : ", nol)
# # # print ("\n=========================")

# # SOAL 12
# # =========================
# #        MENU UTAMA
# # =========================

# # 1. Tampilkan Nama
# # 2. Hitung Umur
# # 3. Keluar

# # Pilih menu : 1

# # Nama saya Risky


# # 1. Tampilkan Nama
# # 2. Hitung Umur
# # 3. Keluar

# # Pilih menu : 2

# # Tahun lahir : 2005

# # Umur anda : 21


# # Pilih menu : 3

# # Program selesai

# print ("=========================")
# print ("        MENU UTAMA       ")
# print ("=========================")

# jalan = True

# while jalan:
    
#     print ("\n1. Tampilkan Nama")
#     print ("\n2. Hitung Umur")
#     print ("\n3. Keluar")

#     pilihan = int(input("Pilih Menu : "))

#     if pilihan == "1":
#         print ("Nama Saya Risky")
#     elif pilihan == "2":
#         print ("Umur 19")
#     elif pilihan == "3":
#         print ("Program Selesai")

#         jalan = False
#     else:
#         print ("Menu Tidak Tersedia")

# SOAL 13

# =========================
#        LOGIN SYSTEM
# =========================

# Username : Risky
# Password : 1234

# Login berhasil!


# Selamat datang Risky

# print ("=========================")
# print ("        LOGIN SYSTEM     ")
# print ("=========================")

# percobaan = 0
# while True:

#     username = input("Username : ")
#     password = input("Password : ")

#     if username == "Risky" and password == "1234":
#         print ("LOGIN BERHASIL!!!")
#         print ("\nSELAMAT DATANG", username)
#         break
#     else:
#         percobaan = percobaan + 1
#         print ("\nLOGIN GAGAL")
#         print ("Percobaan ke-", percobaan)

#         if percobaan == 3:
#             print ("Akun Terkunci")
#             break

# SOAL 14
# =========================
#      KALKULATOR
# =========================

# Angka pertama : 10
# Angka kedua   : 5


# 1. Tambah
# 2. Kurang
# 3. Kali
# 4. Bagi


# Pilih : 1


# Hasil : 15

# print ("=========================")
# print ("        KALKULATOR       ")
# print ("=========================")

# def tambah (a,b):
#     return a + b

# def kurang (a,b):
#     return a - b

# def kali (a,b):
#     return a * b

# def bagi (a,b):
#     return a / b

# angka_pertama = float(input("Masukan Angka Pertama : "))
# angka_kedua = float(input("Masuka Angka Kedua : "))

# print ("\n1. Tambah")
# print ("2. Kurang")
# print ("3. Kali")
# print ("4. Bagi")

# pilih = input("Pilih Sistem Operasi : ")

# if pilih == "1":
#     hasil = tambah(angka_pertama,angka_kedua)
# elif pilih == "2":
#     hasil = kurang(angka_pertama,angka_kedua)
# elif pilih == "3":
#     hasil = kali(angka_pertama,angka_kedua)
# elif pilih == "4":
#     hasil = bagi(angka_pertama,angka_kedua)
# else:
#     print ("Sistem Operasi Tidak Valid")

# print ("Hasil : ", hasil)
    
# SOAL 15
# =========================
#       KASIR SEDERHANA
# =========================

# 1. Tambah Barang
# 2. Lihat Total
# 3. Bayar
# 4. Keluar


# Pilih : 1

# Nama Barang : Buku
# Harga : 15000
# Jumlah : 2


# Barang berhasil ditambahkan


# Pilih : 2


# Total Belanja : 30000


# Pilih : 3

# Uang Bayar : 50000

# Kembalian : 20000


# Pilih : 4

# Program selesai

print ("=========================")
print ("     KASIR SEDERHANA     ")
print ("=========================")

def tambah_barang():
    nama_barang = input("Masukan Nama Barang : ")
    harga = int(input("Masukan Harga Barang : "))
    jumlah = int(input("Jumlah Brang : "))

    subtotal = harga * jumlah
    print ("Sub Total : ", subtotal)

    return subtotal

def bayar(total):
    uang = int(input("Masukan Uang Pembayaran : "))
    kembalian = uang - total

    return kembalian

jalan = True
total = 0

while jalan:
    print ("\n1. Tambah Barang")
    print ("2. Lihat Total")
    print ("3. Bayar")
    print ("4. Keluar")

    pilihan = input("Masuka Pilihan : ")

    if pilihan == "1":
        hasil = tambah_barang()

        total = total + hasil
    
    elif pilihan == "2":
        print ("Total bayar : ", total)
    
    elif pilihan == "3":
        kembali = bayar(total)
        print ("Kembalian : ", kembali)
    
    elif pilihan == "4":
        print ("Program Selesai")

        jalan = False
    
    else:
        print ("Menu Tidak Tersedia")


