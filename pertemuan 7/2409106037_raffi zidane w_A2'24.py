# # # # # # # def menu():
# # # # # # #     print("""
# # # # # # #     menu pilihan
# # # # # # #     1.tambah
# # # # # # #     2.kurang
# # # # # # #     3.kali
# # # # # # #     4.bagi
# # # # # # #     """)

# # # # # # # menu()

# # # # # # # Membuat Fungsi
# # # # # # def salam():
# # # # # #     print ("Selamat Pagi, FT Muda")
# # # # # # def kali():
# # # # # #     x = 6*4
# # # # # #     print(x)
# # # # # # # Pemanggilan Fungsi
# # # # # # salam()
# # # # # # kali()
# # # # # # # Hasilnya:
# # # # # # # Selamat Pagi, FT Muda
# # # # # # # 24

# # # # # # # Pemanggilan Fungsi 3 kali
# # # # # # salam()
# # # # # # salam()
# # # # # # salam()
# # # # # # kali()
# # # # # # kali()
# # # # # # kali()
# # # # # # # Hasilnya:
# # # # # # # Selamat Pagi, FT Muda
# # # # # # # Selamat Pagi, FT Muda
# # # # # # # Selamat Pagi, FT Muda
# # # # # # # 24
# # # # # # # 24
# # # # # # # 24

# # # # # def salam(nama):
# # # # #     print("selamat pagi", nama)
# # # # # salam("jidan")

# # # # # perbedaan mengunakan para meter dan tidadak ialah,jika mengunakan parameter input a bisa di luar kode
# # # # a = int(input("angka 1:"))
# # # # b = int(input("angka 2:")) # input diluar def
# # # # def tambah(a,b):
# # # #     hasil = a + b
# # # #     print(hasil)

# # # # tambah(a,b)

# # # # def penjumlahan():
# # # #     a = int(input("angka 1:"))
# # # #     b = int(input("angka 2:")) # input di dalam def
# # # #     hasil = a + b
# # # #     print(hasil)
# # # # penjumlahan()

# # # # fungsi
# # # a = int(input("angka 1:")) # variabel global
# # # b = int(input("angka 2:")) # bisa di akses semua fungsi

# # # def tambah(a,b):
# # #     hasil = a + b # variabel lokal
# # #     return hasil
# # # print(tambah(a,b))

# # # nama = "shandy"

# # # def salam():
# # #     nama = "ibnu"
# # #     print(nama)

# # # # salam() # prioritas ambil yang lokal, ibnu

# # # rumus: sisi x sisi
# # def luas_persegi(sisi):
# #     luas = sisi * sisi
# #     return luas
# # # rumus: sisi x sisi x sisi
# # def volume_persegi(sisi):
# #     volume = luas_persegi(sisi) * sisi
# #     print ("Volume Persegi = ", volume)
# # # pemanggilan Fungsi
# # volume_persegi(6)

# # fungsi untuk menampilkan semua data
# buku =[]
# def show_data():
#     if len(buku) <= 0:
#         print ("Belum Ada data")
#     else:
#         print("ID", "Nama Buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])
# # fungsi untuk menambah data
# def insert_data():
#     buku_baru = input("Judul Buku : ")
#     buku.append(buku_baru)
# # fungsi untuk edit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         buku[indeks] = judul_baru
# # fungsi untuk menhapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         buku.remove(buku[indeks])
# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")
# while (True):
#     show_menu()