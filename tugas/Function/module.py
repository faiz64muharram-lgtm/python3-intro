import doa_harian
import hitung_uang



doa = doa_harian.doa_tangi()
print(f"Doa harian:{doa}")

doaa= doa_harian.doa_turu()
print(f"Doa harian:{doaa}")


jajankeren = [50000,30000,15000,70000,10000]

print(hitung_uang.tambah_bonus(jajankeren))

import rangking
nilai=[75, 90, 60, 88, 100, 55]

print(rangking.urutkan_nilai(nilai))

print("nilai tertinggi:",rangking.nilai_tertinggi(nilai))

print("nilai terendah:",rangking.nilai_terendah(nilai))
import emoji_mood

emote="-> senang"  "😀","biasa" " 😐","sedih" "😢","semangat" "💪"

mood_list=['senang','biasa','sedih','semangat']

print (emoji_mood.convert_mood(mood_list))











