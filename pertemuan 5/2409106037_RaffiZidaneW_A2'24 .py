# # # #berikut list nama mahasiswa
# # # nama_mhs = [“Celio”, “Afrizal”, “Farrel”, “Ghazali”]
            
# # #  #berikut adalah mendefinisikan list tas
# # # tas = ["buku", 32, True, 3.14, [“IF”, 24]]

# # #berikut adalah contoh menggunakan list tas
# # tas = ["buku", 32, True, 3.14, ["IF", 24]]
# # #disini kita melakukan pemanggilan pada list “tas” untuk elemen yang pertama
# # #karena indels pada python di mulai dari 0, maka kita masukkan angka 0 pada bagian indeks
# # print(tas[0])
# # print(tas[4])

# nama = ["celio","shandy","farel","ghazali","vito","yuyun","adri","rizal","adi","ibnu"]
# matkul = ["apd","apl","basdat","strukturdat","web","jarkom"]

# data = nama+matkul

# print("sebelum: ")
# print(nama)
# print("")
# print("sesudah: ")
# print(data*2)

# # nama.insert(2,"afrizal")
# # print (nama)
# # nama[4]= "fufufafa"
# # del nama[4]= "fufufafa" (delete)
# # hapus = nama.pop(2) (ambil list ke variabel lain)
# # print(nama)
# # print(hapus)
# # print(nama[0:2])
# # print(nama[1:9:2]) (start:slice:step)

# nested list
# data = ["farel","celio",[1,2,["hai",23,2,3,True]]]
# print(data[2][2][1]) # 2 kali index index=[] untuk mengambil list
# print(data[::-1])

# matkul = [1,2,3,4,[5,6,7,[2,3,4]]]
# print(matkul[4][3][1])

# matkul = [[1,2,3,4],[4,6,7],[5,8,9]]
# for i in matkul:
#     for j in i:
#         print(j, end='=') # end buat list menyamping +''

# nama = ('fareel','vito','shandy','rijal')
# print(nama[1])

# #mendeklarasikan tuple
# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
# #lalu kita unpacking
# absen, prodi, nim, nama = mahasiswa
# #maka ketiga variabel tersebut akan berisi data dari tuple mahasiswa
# #menampilkan variabel
# print(absen)
# print(prodi)
# print(nim)
# print(nama)

print(
    """
===========================
   DATA MAHASISWA INFOR
===========================
1.tambah data
2.tampilkan data
3.ubah data
4.hapus
5.keluar 
============================
    """
)
data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for i in range(len(data_mahasiswa)):
            print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("NAMA : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Data Mahasiswa")
        break
    else:
        print("Anda Salah Input")