sayılar = [4,25,673,2,9,0,12,32]
harfler = ["t","u","i","s","p"]
# listelerin eleman sayısını bulalım
print(len(sayılar+harfler))

# listenin en küçük değerli elemanını bulalım: min()
print(min(sayılar))
print(min(harfler))

# listenin en büyük değerli elemanını bulalım : max()
print(max(sayılar))
print(max(harfler))

# metin ve sayılardan oluşan listeleri birleştirip en büyüğünü bulalım
bırlesmıs = sayılar+harfler

# print(max(birlesmis)) hata verdi çünkü str ve int arasaında > , < kullanılamaz

# listenin sonuna yeni eleman ekleyelim: append()
sayılar.append(7)
print(sayılar)

harfler.append("m")
print(harfler)

# listenin istediğimiz konumuna yeni eleman ekleyelim
sayılar.insert(5,8)
print(sayılar)

# listenin sonundaki elemanı silelim: pop()
sayılar.pop()  # konum belirtilebilir
print(sayılar)

# listede belirli bir değere ssahip elamanları silelim
sayılar.remove(25)
print(sayılar)

# listedeki elemanları sıralayalım: sort() # küçükten büyüğe
sayılar.sort()
print(sayılar)

sayılar.reverse()
print(sayılar)

harfler.sort()
print(harfler)

# listedeki isimleri alfabetik sıraya göre sırayalım
isimler = ["İsmail", "Ömer" , "maxkaragüler" ]
isimler.sort()
print(isimler)

# listeyi temizleyelim
isimler.clear()
print(isimler)



































































































