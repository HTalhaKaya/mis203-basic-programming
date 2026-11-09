branslar = ("Yazılım", "Tasarım", "Pazarlama")

tum_ogrenciler = []

print("--- ÖĞRENCİ KAYIT ---")
for i in range(3):
    isim = input(f"{i+1}. öğrencinin adı: ").strip()
    brans = input(f"{i+1}. öğrencinin branşı: ").strip()
    tum_ogrenciler.append([isim, [brans]])

tum_ogrenciler.insert(0, ["Ahmet Başkan", ["Yazılım"]])

print(f"Toplam Kayıtlı Öğrenci Sayısı: {len(tum_ogrenciler)}")

silinecek = input("Silinecek öğrencinin adı: ").strip()
for ogrenci in tum_ogrenciler:
    if ogrenci[0] == silinecek:
        tum_ogrenciler.remove(ogrenci)
        break

cikan = tum_ogrenciler.pop()
print(f"Sistemden en son çıkan öğrenci: {cikan[0]}")

tum_ogrenciler.append(["Burak Tan", ["Tasarım"]])

sirali_kopya = sorted(tum_ogrenciler)
print("Sıralı Kopya (Geçici):", sirali_kopya)
print("Orijinal Liste (Değişmedi):", tum_ogrenciler)

tum_ogrenciler.sort()
print("Kalıcı Sıralanmış Liste:", tum_ogrenciler)
