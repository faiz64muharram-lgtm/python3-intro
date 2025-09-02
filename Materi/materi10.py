import csv


print("_____MATERI 10_____")
print("===================")
file_path=r"C:\Users\Ahmad Faiz Muharram\OneDrive\Desktop\phyton project\filerandom\jajan.csv"
#buka file
file_pesan=open(file_path,"r")
#baca isi file
isi_pesan=file_pesan.read()
#tampilkan output isi pesan
print(f"ISI PESAN => {isi_pesan}")
#tutup pesan
file_pesan.close()

print("-----UPDATE DATA CSV------")

jajan_baru=[6,"ais",10000]
print(f"jajan baru:{jajan_baru}")
#open () -> mebuka filr dari file path
#mode 'a' -> append (tambah data)
#newline-> tamabh baris baru dengan teks kosong
#with ....as ->buka file dengan tutup otomatis

with open(file_path,"a",newline="") as file_pesan:
 
 #aktifkan mode writer csv dari file target
 writer= csv.writer(file_pesan)
 #tambahkan baris dari wariable jajan baru
 writer.writerow(jajan_baru)









