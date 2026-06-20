# # # #SOAL 3
# # # # =========================
# # # #    SISTEM NILAI MAHASISWA
# # # # =========================

# # # # Nama Mahasiswa : Risky
# # # # NIM            : 240040110

# # # # Nilai Tugas    : 85
# # # # Nilai UTS      : 80
# # # # Nilai UAS      : 90

# # # # =========================
# # # # HASIL
# # # # =========================

# # # # Nama : Risky
# # # # NIM  : 240040110

# # # # Nilai Akhir : 85.5
# # # # Grade       : A
# # # # Status      : LULUS

# # # # print ("=========================")
# # # # print ("SISTEM NILAI MAHASISWA")
# # # # print ("=========================")

# # # # nama = input("Nama Mahasiswa : ")
# # # # nim = int(input("Masukan NIM : "))

# # # # tugas = float(input("Masukan Nilai Tugas : "))
# # # # uts = float(input("Masukan Nilai UTS : "))
# # # # uas = float(input("Masukan Nilai UAS : "))

# # # # nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

# # # # if nilai_akhir >= 85:
# # # #     grade = "A"

# # # # elif nilai_akhir >= 75:
# # # #     grade = "B"

# # # # elif nilai_akhir >= 65:
# # # #     grade = "C"

# # # # elif nilai_akhir >= 50:
# # # #     grade = "D"

# # # # else:
# # # #     grade = "E"
    
# # # # if nilai_akhir >= 65:
# # # #     status = "lulus"

# # # # else:
# # # #     status = "tidak lulus"

# # # # print("\n=========================")
# # # # print("HASIL")
# # # # print("=========================")

# # # # print ("\nNama : ", nama)
# # # # print ("NIM : ", nim)
# # # # print("Nilai Akhir :", nilai_akhir)
# # # # print("Grade       :", grade)
# # # # print("Status      :", status)

# # # SOAL 4
# # # =========================
# # #       KALKULATOR
# # # =========================

# # # Angka pertama : 10
# # # Angka kedua   : 5


# # # Pilih operasi:
# # # 1. Tambah
# # # 2. Kurang
# # # 3. Kali
# # # 4. Bagi

# # # Pilihan : 1


# # # Hasil:
# # # 10 + 5 = 15

# # print ("=========================")
# # print ("        KALKULATOR       ")
# # print ("=========================")

# # angka_pertama = float(input("Masukan Angka Pertama : "))
# # angka_kedua = float(input("Masukan Angka Kedua : "))

# # print ("PILIH OPERASI")
# # print ("\n1. Tambah")
# # print ("2. Kurang")
# # print ("3. Kali")
# # print ("4. Bagi")

# # pilih = input("Pilihan : ")

# # if pilih == "1":
# #     tambah = (angka_pertama + angka_kedua)
# #     print ("Hasil : ", tambah)

# # elif pilih == "2":
# #     kurang = (angka_pertama - angka_kedua)
# #     print ("Hasil : ", kurang)
# # elif pilih == "3":
# #     kali = (angka_pertama * angka_kedua)
# #     print ("Hasil : ", kali)
# # elif pilih == "4":
# #     if angka_kedua != 0:
# #         hasil = angka_pertama / angka_kedua
# #         print("Hasil :", hasil)

# #     else:
# #         print("Tidak bisa dibagi dengan 0")
# # else:
# #     print ("PILIHAN TIDAK VALID")

# SOAL 5
# =========================
#     TOTAL BELANJA
# =========================

# Masukkan jumlah barang : 3


# Barang ke-1
# Harga : 10000

# Barang ke-2
# Harga : 20000

# Barang ke-3
# Harga : 15000


# # =========================
# # Total Belanja : 45000
# # =========================

# print ("=========================")
# print ("      TOTAL BELANJA      ")
# print ("=========================")

# total = 0
# jumlah_barang = int(input("Masukan Jumlah Barang : "))
# for i in range(jumlah_barang):

#     harga = int(input("Harga barang ke : "))

#     total = total + harga

# print ("=========================")
# print ("Total Belanja : ", total)
# print ("=========================")
