import csv
print("----MATERI 11---- FILE HANDLING PART 2")
print("UPDATE CSV")
print("=======================================")



file_path_csv=r"C:\Users\Ahmad Faiz Muharram\OneDrive\Desktop\phyton project\filerandom\jajan.csv"
#siapkan data jajan kosong #
# untuk menampung data dari csv ke list
data_jajan=[]
with open (file_path_csv,"r")as file_jajan:
    #csv.reader(-> membaca is file csv)
    isi_file_table=csv.reader(file_jajan)
    #ekstrak semua data debgan for loop
    for item_jajan in isi_file_table:
        print(item_jajan)
        #tamabah item ke list data jajan
        data_jajan.append(item_jajan)

#2. mengubah atau membuat data baru
for baris in data_jajan:
  print(f"Prose item no =>{baris[0]}")
  print(baris)
#jika kolom nama adalah nama "x nama"
  if baris[1] =="Abdul":
     uang_jajan_baru=25000
     baris[2]=uang_jajan_baru
     print(f"DATA DITEMUKAN.....,uang nya:{uang_jajan_baru}")
     #ganti kolom uang jajan dengan nilai baru
     print("_____LOOP END______")

#4.tulis ulang dengan mode 'w' -> write

with open (file_path_csv,"w",newline="")as file_jajan:
   writer=csv.writer(file_jajan)
   #writerows()-> tulis sekali banyak
   writer.writerows(data_jajan)

     