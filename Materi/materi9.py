print("MATERI 9 -> PYTHON 3 fUNCTION")
print("_____________________________")

def say_hello(name):
    #funtion penyimpan kode dan tidak akan dieksekusi jika tidak dipanggil
    print(f"Halo bung....{name}")
    print("KUN ROJULAN")

say_hello_Two=lambda name:print (f"hello cuy....{name}")
#Panggil fungsinya disini
say_hello("Purba")
say_hello("Ardhon")
print("==============")
say_hello_Two("alfiz")
say_hello_Two("ho Yuhao")

#contoh pene rapan lambda dengan higher-order function
#map()--sorted()--filter()



#sorted ()->mengurutkan data

print(f"Doa harian:{doa}")
urutkanUang=sorted(daftar_jajan_mingguan)
print(f"urutkan uang :{urutkanUang}")
UrutanUangTerbalik=sorted(daftar_jajan_mingguan,reverse=True)
print(f"urutkan uang dari yg besar :{UrutanUangTerbalik}")

#map ()-> mentransformasi data
kurangiJajannya=map(lambda uang: uang - 5000,daftar_jajan_mingguan)
list_kurangi_uang=list(kurangiJajannya)
print(f"map uang jajan berkurang: :{list_kurangi_uang}")

#filter menyaring / menfilter data
filter_uangJajan = filter(lambda uang:uang >= 10000,daftar_jajan_mingguan)
listJajanbanyak=list(filter_uangJajan)
print(f"filter jajan diatas 10k:{listJajanbanyak}")

