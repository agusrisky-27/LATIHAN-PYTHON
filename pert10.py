# SOAL 1
# Masukkan Nama Pembeli : Risky
# Masukkan Total Belanja : 600000

# =========================
#       STRUK BELANJA
# =========================

# Nama Pembeli  : Risky
# Total Belanja : 600000
# Diskon        : 60000
# Total Bayar   : 540000

# def hitung_diskon(total_belanja):
#     print ("Total belanja : ", total_belanja)
#     if total_belanja >= 500000:
#         diskon = total_belanja * 10 / 100
#     elif total_belanja >= 250000:
#         diskon = total_belanja * 5 / 100
#     else:
#         diskon = total_belanja * 0 / 100
        

#     total_bayar = total_belanja - diskon
#     return diskon, total_bayar

# nama_pembeli = input("Masukan Nama : ")
# total_belanja = int(input("Masukan Total Belanja : "))

# print ("\n===================")
# print ("   STRUK BELANJA   ")
# print ("===================\n")

# print ("Nama Pembeli : ", nama_pembeli)
# print ("Total Belanja : ", total_belanja)
# diskon, total_bayar = hitung_diskon(total_belanja)
# print ("Diskon : ", diskon)
# print ("Total Bayar : ", total_bayar)


# SOAL 2
# Masukkan Nama Siswa : Risky
# Masukkan Nilai Tugas : 80
# Masukkan Nilai UTS : 75
# Masukkan Nilai UAS : 90

# =========================
#      HASIL PENILAIAN
# =========================

# Nama         : Risky
# Nilai Akhir  : 84.5
# Grade        : B
# Status       : Lulus

def hitung_nilai(nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = (nilai_tugas * 20 / 100) + (nilai_uts * 30 / 100) + (nilai_uas * 50 / 100)
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 75:
        grade = "B"
    elif nilai_akhir >= 65:
        grade = "C"
    elif nilai_akhir >= 50:
        grade = "D"
    else:
        grade = "E"
    
    if nilai_akhir >= 65:
        status = "Lulus"
    else: 
        status = "Tidak Lulus"
    
    return nilai_akhir, grade, status

nama = input("Masukan Nama Siswa : ")
nilai_tugas = float(input("Masukan Nilai Tugas : "))
nilai_uts = float(input("Masukan Nilai UTS : "))
nilai_uas = float(input("Masukan Nilai UAS : "))

print ("\n=======================")
print ("    HASIL PENILAIAN    ")
print ("=======================\n")

print ("Nama : ", nama)
nilai_akhir, grade, status = hitung_nilai(nilai_tugas, nilai_uts, nilai_uas)
print ("Nilai Akhir : ", nilai_akhir)
print ("Grade : ", grade)
print ("Status : ", status)

