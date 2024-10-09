# # # # # # daftar_buku = {
# # # # # # "Buku1" : "Harry Potter", # key=buku1 value=harry potter
# # # # # # "Buku2" : "Percy Jackson",
# # # # # # "Buku3" : "Twillight"
# # # # # # "buku4" : "a darker shade of magic"
# # # # # # }
# # # # # # print(daftar_buku["Buku1"])
# # # # # # print(daftar_buku["Buku2"])
# # # # # # print(daftar_buku["Buku3"])
# # # # # # # jika key sama maka akan ambil yang paling bawah
# # # # # # # value boleh sama

# # # # # # # dictionary kosong
# # # # # # daftar_buku = {}
# # # # # # daftar_buku["Buku1"] = "Harry Potter"
# # # # # # daftar_buku["Buku2"] = "Percy Jackson"
# # # # # # daftar_buku["Buku3"] = "Twillight"
# # # # # # print(daftar_buku)

# # # # # # nested dictionary
# # # # # Biodata = {
# # # # #     "Nama" : "Aldy Ramadhan Syahputra",
# # # # #     "NIM" : 2109106079,
# # # # #     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# # # # #     "Mahasiswa_Aktif" :True,
# # # # #     "Social Media" : {
# # # # #         "Instagram" : "@aldyrmdhns_",
# # # # #         "Discord" : "\'Izanami#6848"
# # # # #     }
# # # # # }

# # # # # print(Biodata['Social Media']['Discord']) #nested dictionary
# # # # # print(Biodata['KRS'][0]) #dictionary of list
# # # # # print(Biodata.get('krs'))

# # # # Nilai = {
# # # #     "Matematika" : 80,
# # # #     "B. Indonesia" : 90,
# # # #     "B. Inggris" : 81,
# # # #     "Kimia" : 78,
# # # #     "Fisika" : 80
# # # # }
# # # # print("Jumlah Nilai =", len(Nilai))
# # # # # print(Nilai)

# # # # # Nilai["Sejarah"] = 100
# # # # # print(Nilai)

# # # # # Nilai["Fisika"] = 100
# # # # # print(Nilai)

# # # # # Nilai.update({"biologi" : "89"})
# # # # # print(Nilai)

# # # # # del Nilai["biologi"]
# # # # # print(Nilai)

# # # # # Simpan = Nilai.pop("Fisika")
# # # # # print(Nilai)
# # # # # print(Simpan)

# # # # # Nilai.clear

# # # # # #tanpa menggunakan items
# # # # # for i in Nilai:
# # # # #     print(i)

# # # # # print("")

# # # # # #menggunakan items
# # # # # for i, j in Nilai.items():
# # # # #     print(f"Nilai {i} anda adalah {j}")

# # # # copy and fromkeys
# # # Buku = {
# # #     "No Longer Human" : "Osamu Dazai",
# # #     "Harry Potter" : "J.K. Rowlings",
# # #     "Hamlet" : "William Shakespeare"
# # # }
# # # pinjam = Buku.copy()
# # # print("Dictionary yang Telah Disalin : ", pinjam)

# # # key = "apel", "jeruk", "mangga"
# # # value = 1
# # # buah = dict.fromkeys(key, value)
# # # print(buah)

# # Nilai = {
# #     "Matematika" : 80,
# #     "B. Indonesia" : 90,
# #     "B. Inggris" : 81,
# #     "Kimia" : 78,
# #     "Fisika" : 80
# # }
# # #menggunakan keys
# # for i in Nilai.keys():
# #     print(i)

# # print("")

# # #menggunakan value
# # for i in Nilai.values():
# #     print(i)

# # set default
# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81
# }

# #sebelum Setdefault
# print(Nilai)
# print("")

# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")

# #setelah menggunakan setdefault
# print(Nilai)

Musik = {
    "The Chainsmoker" : ["All we Know", "The Paris"],
    "Alan Walker" : ["Alone", "Lily"],
    "Neffex" : ["Best of Me", "Memories"]
}

for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
    print("")