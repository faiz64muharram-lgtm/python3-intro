print("materi python data structure")
print("____________________________")

#list [] berurutan,bisa diubah,boleh duplikat.
daftar_belanja=["teh desa","naspad","nasgor"]

#memilih list yg mau di pilih
print("isi dompet",daftar_belanja)
print("item-1",daftar_belanja[0])
print("item-1",daftar_belanja[1])

#menambahkan item baru ke list
daftar_belanja.append("mie ayam")
daftar_belanja.append("baso")
print("daftar belanja sekarang",daftar_belanja)
print(daftar_belanja[4])
#menghapus item dari list
daftar_belanja.remove("baso")
print("isi tas belanja akhir",daftar_belanja)
print("___TUPLE___")

#tuple:beruurutan,tak bisa diubah,boleh duplikat
#penulisannya dengan ()

ttl= ("bandung",4,"januari",2010)
print("tanggal lahir agus",ttl)

#[no index] akses data tuple

print("tanggal:",ttl[0])
print("bulan:",ttl[1])
print("Tahun:",ttl[2])
#akses bulan(posisi index) :lalu batas akhir item nya

print("bulan tahun:",ttl[1:3])

#unpacking tuple ke variabel baru
tempat_lahir,tanggal_lahir,bulan_lahir,tahun_lahir= ttl
print(tempat_lahir)
print(tahun_lahir)

#manipulasi list lanjutan

jajan_agus=["pentol","naspad"]
jajan_jaki=["nasgor","baso",10000]
jajan_agus_dan_jaki=jajan_agus+jajan_jaki
print(jajan_agus_dan_jaki)
#list multi dimensi

list_minuman = [
    ["kopi","jasjus","teh warga"],#baris0
    ["jus apel","jus lemon"],#1
    ["es teler"],#2
]
#tiap baris punya 3 index
print(list_minuman)
print(list_minuman[0][2])






