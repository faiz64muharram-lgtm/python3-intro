import csv

file_path=r"C:\Users\Ahmad Faiz Muharram\OneDrive\Desktop\phyton project\filerandom\murojaah bos\data.csv"

with open(file_path,"r") as file_baru:
    next(file_baru)
    read= csv.reader (file_baru)
    list_read= list(read)



print("SEMUA DATA")
print("="*15)
for baris in list_read:
    nomor=baris[0]
    nama=baris[1]
    kelas=baris[2]

    print(f"{nomor}|{nama}|{kelas}")