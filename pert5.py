# SOAL 16
# =========================
#    DATA MAHASISWA
# =========================

# 1. Tambah Data
# 2. Tampilkan Data
# 3. Cek Status Nilai
# 4. Keluar


# Pilih : 1

# Nama : Risky
# NIM : 240040110
# Nilai : 85

# Data berhasil ditambahkan


# Pilih : 2


# =========================
# DATA
# =========================

# Nama  : Risky
# NIM   : 240040110
# Nilai : 85


# Pilih : 3


# Nilai : 85

# Status : Lulus


# Pilih : 4

# Program selesai

print("=========================")
print("   DATA MAHASISWA")
print("=========================")



nama = ""
nim = ""
nilai = 0



def tambah_data():

    global nama
    global nim
    global nilai


    nama = input("Nama : ")

    nim = input("NIM : ")

    nilai = int(input("Nilai : "))


    print("Data berhasil ditambahkan")




def tampil_data():


    print("=========================")
    print("DATA")
    print("=========================")


    print("Nama :", nama)
    print("NIM :", nim)
    print("Nilai :", nilai)




def cek_nilai(nilai):


    if nilai >= 65:

        return "Lulus"


    else:

        return "Tidak Lulus"




jalan = True


while jalan:


    print("\n1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Cek Status Nilai")
    print("4. Keluar")


    pilihan = input("Pilih : ")



    if pilihan == "1":

        tambah_data()



    elif pilihan == "2":

        tampil_data()



    elif pilihan == "3":

        hasil = cek_nilai(nilai)

        print("Status :", hasil)



    elif pilihan == "4":

        print("Program selesai")

        jalan = False



    else:

        print("Menu tidak tersedia")

