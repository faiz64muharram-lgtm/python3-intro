print("Tantangan 1 JADWAL PIKET ASRAMA")#list
print("===============================")
print("Jadwal piket asrama:")

namasantri=["Faiz","juna","Ahmad"]

for nama in namasantri:
    print("-",nama)
    
print("____Rukun Islam And Iman____")#tuple
print("============================")
print("Rukun Islam:")
rukun_islam = ('Syahadat', 'Shalat', 'Zakat', 'Puasa', 'Haji')

for i, rukun in enumerate(rukun_islam, start=1):
    print(f"{i}.{rukun}")

print("Rukun Iman:")

rukun_iman=("Iman kpd Allah","Iman kpd Malaikat","Iman kpd kitab-kitab Allah","Iman kpd Rosul","Iman kpd Hari kiamat","Iman kpd takdir")

for i in range (len(rukun_iman)):
    
    print(f"{i+1}. {rukun_iman[i]}")


print("KITAB YANG DIPELAJARI")
print("=====================")
print ("KITAB YG DIPELAJARI:")#set

kitab_pelajaran = {'Kitab Tajwid', 'Kitab Fiqh', 'Kitab Aqidah'}
for i in kitab_pelajaran:

    print(f"-{i}")

print("BIODATA SANTRI")
print("==============")
print("Biodata santri:")
biodata ={
    "nama":"Ahmad Faiz Muharram",
    "kelas":"10 A",
    "hafalan":"21 JUZ",

}

for key ,value in biodata.items():
    print(f'-{key}:{value}')

print("=============TAMAT===================")