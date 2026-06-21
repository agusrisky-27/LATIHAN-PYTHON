# SOAL 11
# =========================
#       STATISTIK ANGKA
# =========================

# Masukkan jumlah angka : 6


# Angka ke-1 : 10
# Angka ke-2 : -5
# Angka ke-3 : 0
# Angka ke-4 : 20
# Angka ke-5 : -3
# Angka ke-6 : 8


# =========================
# HASIL
# =========================

# Jumlah Positif : 3
# Jumlah Negatif : 2
# Jumlah Nol     : 1

# =========================

print ("=========================")
print ("     STATISTIK ANGKA     ")
print ("=========================")

positif = 0
negatif = 0
nol = 0 

jumlah_angka = int(input("Masukan Jumlah Angka : "))
for i in range(jumlah_angka):
    angka = int(input("Masukan angka : "))

    if angka > 0:
        positif = positif + 1
    elif angka < 0:
        negatif = negatif + 1
    else:
        nol = nol + 1


print ("=========================")
print ("          HASIL          ")
print ("=========================")
print ("\nJumlah Positif : ", positif)
print ("Jumlah Negatif : ", negatif)
print ("Jumlah Nol : ", nol)
print ("\n=========================")