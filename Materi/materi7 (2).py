print("materi 7 _ PYTHON DATA STRUCTURE")

#set -> {} -> tidak brurutan, bisa berubah , tidak duplikat

game_abdul= {"roblox","citampi","delta"}
game_ardon= {"FF","cod","roblox"}

game_abdul.add("citampi")
game_ardon.add("ML")
game_abdul.remove("delta")

print("game abdul:",game_abdul)
print("game ardon:",game_ardon)
gabungan= game_abdul | game_ardon
print("game gabungan:",gabungan)

#for (loop) untuk mengeluarkan isi item dari set

for game in gabungan:
    print(game)
    print("--> game terpilih:",game)
    print("---> transfer data",game,"ke XBOX ONE")


#dictionary (dict) -> {key:value} / {kunci:isi}
#--> berurutan , berubah,tidak dupilkat

kamus_anime={
    "one_piace" : "monkey D luffy",
    "blue_lock" : "isagi",
    "demon_slayer" : "tanjidor",
    "waifu":{
        "one piace":"rebbecca",
        "demon slayer":"shinobu",
    }
}
print("kamus anime:",kamus_anime)
print("MC blue lock:", kamus_anime["blue_lock"])
print("waifu demon slayer;",kamus_anime["waifu"]["demon slayer"])


#nambah item di dictionary
kamus_anime["naruto"]= "jiraiya"
print("mc naruto:",kamus_anime["naruto"])
#mengubah-----------------
kamus_anime["blue_lock"]= "inosuke"
print(kamus_anime)

#menghapus----------------

del(kamus_anime)["demon_slayer"]
print("kamus anime terbaru:",kamus_anime)