# MATERI PARAETER

# SOAL 1
# Masukkan Nama : Risky

# Halo, selamat datang Risky

# def login(nama):
#     print ("Halo, selamat datang", nama)

# nama = input("Masukan Nama :")

# login(nama)


# SOAL 2
# Masukkan Nama : Risky
# Masukkan Umur : 19

# ====================
# BIODATA
# ====================

# Nama : Risky
# Umur : 19

# def biodata(nama, umur):
#     print ("\n==================")
#     print ("      BIODATA     ")
#     print ("==================\n")
#     print ("Nama : ", nama)
#     print ("Umur : ", umur)

# nama = input ("Masukan Nama :")
# umur = int(input ("Masukan Umur :"))

# biodata(nama, umur)

# SOAL 3
# Panjang : 10
# Lebar : 5

# Luas Persegi Panjang : 50

# def luas(panjang, lebar, luas_persegi_panjang):
#     print ("Panjang : ", panjang)
#     print ("Lebar : ", lebar)
#     print ("Luas Persegi Panjang ; ", luas)

# panjang = int(input("Masukan Panjang Persegi :"))
# lebar = int(input("Masukan Lebar Persegi :"))
# luas_persegi_panjang = panjang * lebar

# luas(panjang, lebar, luas_persegi_panjang)

# SOAL 4
# Nama : Risky
# Gaji Pokok : 5000000
# Bonus : 1000000

# Total Gaji : 6000000

# def hitung_gaji(nama, gaji_pokok, bonus):
#     print ("Nama :", nama)
#     print ("Gaji Pokok :", gaji_pokok)
#     print ("Bonus :", bonus)

# nama = input("Masukan Nama : ")
# gaji_pokok = int(input("Masukan Gaji Pokok : "))
# bonus = int(input("Masukan Bonus : "))

# hitung_gaji(nama, gaji_pokok, bonus)

# total = gaji_pokok + bonus
# print ("Total Gaji : ", total)

# SOAL 5
# Nama : Risky
# Nilai : 80

# Status : Lulus

def cek_nilai (nama, nilai):
    print ("Nama : ", nama)
    print ("Nilai : ", nilai)

nama = input("Masukan Nama : ")
nilai = float(input("Masukan Nilai : "))

cek_nilai(nama, nilai)

if nilai >= 65:
    print ("Lulus")
else:
    print ("Tidak Lulus")

