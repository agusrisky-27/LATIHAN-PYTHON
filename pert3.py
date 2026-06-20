# # # # # # # # SOAL 6

# # # # # # # # =========================
# # # # # # # #     HITUNG NILAI
# # # # # # # # =========================

# # # # # # # # Masukkan jumlah nilai : 3


# # # # # # # # Nilai ke-1 : 80
# # # # # # # # Nilai ke-2 : 90
# # # # # # # # Nilai ke-3 : 70


# # # # # # # # =========================
# # # # # # # # Total Nilai : 240
# # # # # # # # Rata-rata   : 80
# # # # # # # # =========================


# # # # # # # print ("=========================")
# # # # # # # print ("       HITUNG NILAI      ")
# # # # # # # print ("=========================")

# # # # # # # total = 0
# # # # # # # jumlah_nilai = int(input("Masukan Jumlah Nilai : "))

# # # # # # # for i in range(jumlah_nilai):
# # # # # # #     nilai = int(input("Nilai ke : "))

# # # # # # #     total = total + nilai
# # # # # # #     rata  = total / jumlah_nilai

# # # # # # # print ("=========================")
# # # # # # # print ("Total Nilai : ", total)
# # # # # # # print ("Rata-Rata : ", rata)
# # # # # # # print ("=========================")

# # # # # # SOAL 7
# # # # # # =========================
# # # # # #    CEK ANGKA
# # # # # # =========================

# # # # # # Masukkan jumlah angka : 5


# # # # # # Angka ke-1 : 10
# # # # # # Angka ke-2 : 7
# # # # # # Angka ke-3 : 4
# # # # # # Angka ke-4 : 9
# # # # # # Angka ke-5 : 2


# # # # # # =========================
# # # # # # HASIL
# # # # # # =========================

# # # # # # Jumlah angka genap : 3
# # # # # # Jumlah angka ganjil : 2

# # # # # # =========================

# # # # # print ("=========================")
# # # # # print ("        CEK ANGKA        ")
# # # # # print ("=========================")

# # # # # genap  = 0
# # # # # ganjil = 0
# # # # # jumlah_nilai = int(input("Masukan Jumlah Nilai : "))

# # # # # for i in range(jumlah_nilai):
# # # # #     nilai = int(input("Nilai ke : "))

# # # # #     if nilai % 2 == 0:
# # # # #         genap = genap + 1
# # # # #     else:
# # # # #         ganjil = ganjil + 1

# # # # # print ("=========================")
# # # # # print ("          HASIL          ")
# # # # # print ("=========================")

# # # # # print ("\n=========================")
# # # # # print ("Jumlah Angka Genap : ", genap)
# # # # # print ("Jumlah Angka Gnajil : ", ganjil)
# # # # # print ("=========================")

# # # # SOAL 8
# # # # =========================
# # # #       NILAI TERBESAR
# # # # =========================

# # # # Masukkan jumlah nilai : 5

# # # # Nilai ke-1 : 80
# # # # Nilai ke-2 : 95
# # # # Nilai ke-3 : 70
# # # # Nilai ke-4 : 88
# # # # Nilai ke-5 : 90


# # # # =========================
# # # # HASIL
# # # # =========================

# # # # Nilai terbesar : 95

# # # # =========================

# # # # print ("=========================")
# # # # print ("      NILAI TERBESAR     ")
# # # # print ("=========================")

# # # # terbesar = 0
# # # # jumlah_nilai = int(input("Masukan Jumlah Nilai : "))

# # # # for i in range(jumlah_nilai):
# # # #     nilai = int(input("Nilai ke : "))

# # # #     if nilai > terbesar:
# # # #         terbesar = nilai

# # # # print ("=========================")
# # # # print ("           HASIL         ")
# # # # print ("=========================")
# # # # print ("\nNilai Terbesar : ", terbesar)
# # # # print ("\n=========================")

# # # SOAL 9 
# # # =========================
# # #       NILAI TERKECIL
# # # =========================

# # # Masukkan jumlah nilai : 5

# # # Nilai ke-1 : 80
# # # Nilai ke-2 : 95
# # # Nilai ke-3 : 70
# # # Nilai ke-4 : 88
# # # Nilai ke-5 : 90


# # # =========================
# # # HASIL
# # # =========================

# # # Nilai terkecil : 70

# # # =========================

# # # print ("=========================")
# # # print ("      NILAI TERKECIL     ")
# # # print ("=========================")

# # # terkecil = None
# # # jumlah_nilai = int(input("Masukan Jumlah Nilai : "))

# # # for i in range(jumlah_nilai):
# # #     nilai = int(input("Nilai ke : "))

# # #     if terkecil is None:
# # #         terkecil = nilai
# # #     elif nilai < terkecil:
# # #         terkecil = nilai

# # # print ("=========================")
# # # print ("           HASIL         ")
# # # print ("=========================")
# # # print ("\nNilai Terkecil : ", terkecil)
# # # print ("\n=========================")

# # SOAL 10
# # =========================
# #      STATISTIK NILAI
# # =========================

# # Masukkan jumlah nilai : 5


# # Nilai ke-1 : 80
# # Nilai ke-2 : 90
# # Nilai ke-3 : 75
# # Nilai ke-4 : 85
# # Nilai ke-5 : 70


# # =========================
# # HASIL
# # =========================

# # Total Nilai     : 400
# # Rata-rata       : 80
# # Nilai Tertinggi : 90
# # Nilai Terendah  : 70

# # =========================

# print ("=========================")
# print ("    STATISTIK NILAI      ")
# print ("=========================")

# total = 0
# terbesar = float("-inf")
# terkecil = float("inf")
# jumlah_nilai = int(input("Masukan Jumlah Nilai : "))

# for i in range(jumlah_nilai):
#     nilai = int(input("Masukan Nilai : "))

#     total = total + nilai
#     rata = total / jumlah_nilai

#     if nilai > terbesar:
#         terbesar = nilai
        
#     if nilai < terkecil:
#         terkecil = nilai

# print ("=========================")
# print ("          HASIL          ")
# print ("=========================")
# print ("\nTotal Nilai : ", total)
# print ("Rata-Rata : ", rata)
# print ("Terbesar : ", terbesar)
# print ("Terkecil : ", terkecil)
# print ("=========================")
