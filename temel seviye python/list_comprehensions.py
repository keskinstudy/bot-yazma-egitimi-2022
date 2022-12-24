# 100-200 arasındaki sayıları numaralar değişkenine aktaralım
numaralar = []
for syi in range(100,200):
    numaralar.append(syi)

print(numaralar)



# yukarıdaki işlemi list comprehensions şeklinde yapalım

numaralar2 = [sayi for sayi in range(100,200)]
print(numaralar2)

# 100-200 arasındaki çift sayıları bir listeye aktaralım
cift_sayılar = [sayi for sayi in range(100,200) if sayi % 2 == 0 ]
print(cift_sayılar)

# 100 - 200 arasındaki tek sayıları "{sayı} tek" ciftleri "{sayı} cift" seklinde listeye aktaralım
numaralar3 = [f"{sayi} TEK " if sayi % 2 == 1 else f"{sayi} ÇİFT" for sayi in range(100,200)]
print(numaralar3)

# aşağıdaki işlelmi list comprehensions ilw yapalım
liste = []
for x in range(3):
    for y in range(3):
        liste.append((x,y))
print(liste)

liste2 = []

    










































