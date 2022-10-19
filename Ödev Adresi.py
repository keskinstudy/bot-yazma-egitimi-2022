url = "https://teknolojiaihl.meb.k12.tr"

# 1- "url" içinde kaç karakter olduğunu yazdır.
print(len(url))

# 2- "url" içindeki "meb" sözcüğünü ekrana yazdırın.

# 3- "url" içindeki "k12" sözcüğünü ekrana yazdırın.

# 4- Kullanıcıdan adını, en sevdiği yemeği alın ve cümle içinde yazdırın.
# ÖRNEK CÜMLE: Adınız: Eren. En sevdiğiniz yemek: Pırasa

# 5- Öğrencinin 2 sınav notunu alın. Notunu hesaplayıp cümle içinde yazdırın.
# 1. sınav oranı: %35
# 2. sınav oranı: %65
# ÖRNEK CÜMLE: 1. sınav: 70 puan, 2. sınav: 90 puan, Notunuz: 83.0

# 6- Kullanıcının adını alın ve yan yana 100 defa yazdırın.

#1
print((len(url)))
#2
print(url[22])
print(url[23])
print((url[24]))
#3
print(url[26])
print(url[27])
print(url[28])
#4
name = input("isminiz:")
yemek = input("en sevdiğiniz yemek:")
print(f"adınız {name} en sevdiğiniz yemek {yemek}")
#5
sinav1_yuzde = 0.35
sinav2_yuzde = 0.65
print((60*sinav1_yuzde)+(15*sinav2_yuzde))
#6
isim = input("isminiz:")
print(isim*100)






