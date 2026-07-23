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
    diskon = 10 / 100
    elif total_belanja >= 250000:
        diskon = 5 / 100
    else:
        diskon = 0 / 100
    
    total_bayar = total_belanja * diskon
    return diskon, total_bayar

total_belanja = input("Masukan Nama : ")
nama_pembeli = int(input("Masukan Total Belanja : "))






