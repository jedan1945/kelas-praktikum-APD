# ulang = 10
# for i in range(ulang):
# print("Perulangan ke-" + str(i))

# print halo dulu 12x baru hai
# for j in range (12): # jika (2,12) mk hanya 2-12(10x perulangan)
#     print("halo")
# print("hai")

# pakai list
# 1
# simpan = [12, "udin petot", 14.5, True, 'A']
# for i in simpan:
#     print(i)

# 2
# print("=============")
# print("menu rm sikma")
# print("=============")
# simpan = ["nasgor rizz", "migor ohio", "mie ayam asli nganjuk", "bakso", "esteh"]
# for i in simpan:
#     print(i)

# 3
# print("=============")
# print("menu rm sikma")
# print("=============")
# simpan = ["nasgor rizz", "migor ohio", "mie ayam asli nganjuk", "bakso", "esteh"]
# for i, menu in enumerate(simpan,start=1):
#     print(f"{i}.{menu}")

# 4
# print("=============")
# print("menu rm sikma")
# print("=============")
# simpan = ["nasgor rizz", "migor ohio", "mie ayam asli nganjuk", "bakso", "esteh"]
# for i in range(len(simpan)):
#     print(f"{i+1}.{simpan[i]}")

# nested loop
# for i in range(1, 4): # 1-3 perulangan i menghabiskan dulu perulangan j 1x1 1x2 1x3
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")
#     print()

# makanan = ["mie","sop","bakso"]
# minuman = ["es teh","air putih","es jeruk"]

# while True:
#     print("hello world")

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya' or jawab == 'Ya'):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total perulangan: {hitung}") # kalau print setara jawab,tiap ya adda ttl perulangan.

# i = 0 
# while i<5:
#     print(i)
#     i += 1

# print(“Daftar bilangan ganjil dari 1-10”)
# for i in range(10):
# if i % 2 == 0:
# continue
# print(i)

# print("Daftar bilangan prima dari 1-10")
# for i in range(10):
#     if i % i == 1 or i % 1 == i :

# for i in range(3):
#     print(i)

count = 0
while count < 3:
    print(count)
    count += 1