import json
print("----MATERI 12----JSON FILE HANDLING PART 2")
print("READ JSON")
print("=======================================")

file_path_json=r"C:\Users\Ahmad Faiz Muharram\OneDrive\Desktop\phyton project\filerandom\materi1.json"

#siapkan data jajan kosong #

data_jajan=[]
with open (file_path_json,"r")as file_jajan:
    #json-load(-> membaca is file json)
    isi_file_table=json.load(file_jajan)
    "akse data json dengan key nya"
    print(f"Judul berkas: {isi_file_table["title"]}")
    print(f"Total santri:{isi_file_table["total"]}")
    print(f"Total santri:{isi_file_table["Status santri"]}")
    print(f"Total santri:{isi_file_table["Status lulus"]}")
    print(f"Total santri:{isi_file_table["pelajaran"]}")
    
    #ekstrak data list dengan for loop

    for pelajaran in isi_file_table['pelajaran']:
        print(f"---->{pelajaran}")

print("-"*50)
print("|No|Nama Surah|Ayat|Tempat Turun")
print("-"*50)

for surah in isi_file_table['surah']:
    print(f"{surah['no']}|{surah["nama"]}|{surah["ayat"]}|{surah["Turun"]}|")
