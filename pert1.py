# # # print("=====FORM BIODATA=====")

# # # nama = input("nama : ")
# # # jurusan = int(input("jurusan : "))
# # # umur = input("umur : ")
# # # angkatan = input("angkatan : ")

# # # #gunakan \n untuk memberika brake atau jarak
# # # print("\n=====BIODATA ANDA=====")
# # # print ("nama     :", nama)
# # # print ("jurusan  :", jurusan)
# # # print ("umur     :", umur)
# # # print ("angkatan :", angkatan)

# # SOAL 1
# # =========================
# #       KASIR SEDERHANA
# # =========================

# # Nama barang : Laptop
# # Harga       : 7500000
# # Jumlah      : 2

# # -------------------------
# # Barang : Laptop
# # Harga  : Rp7500000
# # Jumlah : 2

# # Total : Rp15000000

# # Diskon 10%
# # Potongan : Rp1500000

# # Bayar : Rp13500000
# # =========================
# # Terima kasih
# # =========================

# # DONE
# # print ("=========================")
# # print ("FORM KASIR SEDERHANA")
# # print ("=========================")

# # barang = input ("Barang : ")
# # harga = int (input("Harga : "))
# # jumlah = int (input("Jumlah : "))

# # total = (harga * jumlah)
# # diskon = int(0.1 * total)
# # bayar = int(total - diskon)

# # print ("\n=========================")
# # print ("KASIR SEDERHANA")
# # print ("=========================")

# # print ("\nBarang      : ", barang)
# # print ("Harga         : ", harga)
# # print ("Jumlah        : ", jumlah)

# # print ("Total         : ", total)
# # print ("Potogan Harga : ", diskon)
# # print ("Bayar         : ", bayar)

# # print ("\n=========================")
# # print ("TERIMA KASIH")
# # print ("=========================")


# SOAL 2
# =========================
#        ATM SEDERHANA
# =========================

# Masukkan nama : Risky
# Masukkan PIN  : 1234

# Login berhasil!

# Saldo anda : Rp5000000

# Menu:
# 1. Cek Saldo
# 2. Tarik Tunai
# 3. Setor Tunai
# 4. Keluar

# Pilih menu : 2

# Jumlah tarik : 1000000

# Berhasil tarik uang

# # Sisa saldo : Rp4000000

# print ("=========================")
# print ("ATM SEDERHANA")
# print ("=========================")

# nama = input ("Masukan Nama Anda : ")
# pin = input ("Masukan PIN Anda : ")
# saldo = 5000000

# if pin == "1234":
#     print ("\nLogin Berhasil!")

#     print ("\nSaldo Anda : ",saldo)

#     print ("\n1. Cek Saldo")
#     print ("2. Tarik Tunai")
#     print ("3. Setor Tunai")
#     print ("4. Keluar")

#     pilihan = input("\nPilih Menu : ")

#     if pilihan == "1":
#         print ("Saldo Anda : ", saldo)
    
#     elif pilihan == "2":
#         tarik = int(input("Masukan Nominal Tarik Tunai : "))
#         if tarik <= saldo:
#             jumlah_tarik = saldo - tarik
#             print ("Jumlah Tarik : ", tarik)
#             print ("\nSisa Saldo Anda : Rp.", jumlah_tarik)
#         else:
#             print ("Saldo Tidak Cukup")
    
#     elif pilihan == "3":
#         setor = int(input("Masukan Jumlah Setoran : "))
#         if setor <= saldo:
#             jumlah_setor = saldo + setor
#             print ("Jumlah Setoran : ", setor)
#             print ("\nSisa Saldo Anda : Rp.", jumlah_setor)

#     elif pilihan == "4":
#         print ("BERHASIL KELUAR")

#     else:
#         print ("Menu Tidak Tersedia")

# else:
#     print ("\nLogin Gagal!!!")
#     print ("Mohon Periksa Kembali PIN Anda")







