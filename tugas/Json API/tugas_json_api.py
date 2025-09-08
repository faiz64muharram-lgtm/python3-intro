print("TUGAS JSON AND API")
print("-"*20)
import json

total=0
belum_dikembalikan=0
print("Belum kembali:")

with open(r"C:\Users\Ahmad Faiz Muharram\OneDrive\Desktop\Json And API\tugas.json") as data_path:

    item=json.load (data_path)

for anggota in item["anggota"]:
    for kitab in anggota["pinjam"]:
        total +=1
        if kitab["kembali"] == False:
            belum_dikembalikan += 1
            print(f"- {anggota['nama']} : {kitab['judul']} ({kitab['tanggal']})")

print(f"Total dipinjam: {total} | Belum kembali: {belum_dikembalikan}")
  
import requests

#ayat kursi
print("Tugas Json via api")
print("="*20)

url=f"https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
response=requests.get(url)
data_json = response.json()

nama_surat = data_json["data"]
print(f"Ayat Al-Kursi (2:225) -Arab : {nama_surat["text"]}")

#Terjemahan b.ingris
url=f"https://api.alquran.cloud/v1/ayah/2:255/en.asad"
response=requests.get(url)
data_json = response.json()

nama_surah = data_json["data"]
print(f"Terjemah (EN) : {nama_surah["text"]}")
        
            















