print("___PENGULANGAN DICTIONARY_____")
fazzi=[15,"bogor",'dong er']
fazzy = {
    "umur":15,
    "asal":"planet bekasi",
    "waifu":"dong er",
}

print(fazzi[0])

#operasi pada dictionary
#1.mengakses nilainya

print(fazzy["waifu"])

#2.nambahin item (value) 

fazzy["husbu"]="ho yuhou"
print(fazzy)

print(fazzy["husbu"])
#3. mengubah value

fazzy["waifu"]="nang jian jian"

print(fazzy["waifu"])

#4.menghapus nilai

del(fazzy["asal"])
print(fazzy)

#

print("waifu"in fazzy)

#6.cara mendapakatkan key dan value nya

#.cara ngecek key nya

print(fazzy.keys())

#cara ngecek valuenya

print(fazzy.values())

#looping

for key in fazzy:
    print(key)

for value in fazzy.values():
    print(value)

for key, value in fazzy.items():
    print(f"{key} -->  {value}")
    #
kelas={
    "siswa":{
        "nama":"ais",
        "umur":13,
        "asal":"tegal"

    },

    "siswa2":{
        "nama":"faiz",
        "umur":15,
        "asal":"bekasi"
    }
}

print(kelas["siswa"])