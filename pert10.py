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

def hitung_diskon(total_belanja):
    print ("Total belanja : ", total_belanja)
    if total_belanja >= 500000:
        diskon = total_belanja * 10 / 100
    elif total_belanja >= 250000:
        diskon = total_belanja * 5 / 100
    else:
        diskon = total_belanja * 0 / 100
        

    total_bayar = total_belanja - diskon
    return diskon, total_bayar

nama_pembeli = input("Masukan Nama : ")
total_belanja = int(input("Masukan Total Belanja : "))

print ("\n===================")
print ("   STRUK BELANJA   ")
print ("===================\n")

print ("Nama Pembeli : ", nama_pembeli)
print ("Total Belanja : ", total_belanja)
diskon, total_bayar = hitung_diskon(total_belanja)
print ("Diskon : ", diskon)
print ("Total Bayar : ", total_bayar)






