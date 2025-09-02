faiz = ["pelajar",15,False]
print(faiz)

#operasi dasar pada list

#1.mengakses elemen [index]
print(faiz[1])
#mengubah nilainya
faiz[0]= 'pekerja'
print(faiz)
#menambah elemen
faiz.append("the best")
print(faiz)
#nambahin ke index yg kita mau

faiz.insert(0,"gamers")
print(faiz)
#menghapus elemen

#menghapus berdasrkan isi
faiz.remove("pekerja")
print(faiz)
#menghapus berdasarkan index
faiz.pop(0)
print(faiz)

#5.panjang list

print(len(faiz))

#6.mencetak seluruh isi list menggunakan looping
for item in faiz:
    print(item)