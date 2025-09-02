import csv

file_path=r"C:\Users\Ahmad Faiz Muharram\OneDrive\Desktop\phyton project\filerandom\tugas csv\tugas.csv"

with open(file_path,"r") as file_baru:
    next(file_baru)
    read=csv.reader (file_baru)
    list_read=list(read)

    print("TANGGAL|KETERANGAN|KATEGORI|JUMLAH")

    for baris in list_read:
        TANGGAL=baris[0]
        KETERANGAN=baris[1]
        KATEGORI=baris[2]
        JUMLAH=baris[3]

        print(f"{TANGGAL}|{KETERANGAN}|{KATEGORI}|{JUMLAH}")


with open(file_path,"a",newline="") as file_pesan:
 
 
 writer= csv.writer(file_pesan)
 
 writer.writerow({"10",'magelang',"abdul"})
 


