okul = "Sancaktepe Teknoloji Anadolu İmam Hatip Lisesi"
# tüm karakterleri büyük harf yapalım
print((okul.upper()))
# tüm harfler küçük
print(okul.lower())
# kelimenin ilk harfi büyük
print(okul.title())
# karakter dizisinin ilk karakterini büyük diğer karakterlerini küçük yapalım
print(okul.capitalize())
# belirli bir ifadenin kaç defa yer aldığını bulalım ilk önce tüm harfleri küçültelim ki büyük küçük duyarlılığına takılmayalım
print(okul.lower().count("e"))
# soldaki ve sağdaki boşluk karakterlerini temizleyelim
name = input("adınız:")
print(name.strip())
# soldaki ve sağdaki belirli karakterleri temizleyelim
urun_kodu = "HEP20221022HEP"
print(urun_kodu.strip("HEP"))
# soldaki boşluk ve karakterleri temizler
print(urun_kodu.lstrip("HEP"))
# sağdaki boşluk ve karakterleri siler
print(urun_kodu.rstrip("HEP"))
# karakter dizisini bölelim (ürün kodu değişkeninde olmaz çünkü boşluk yok)
# split(.) olursa boşluklardan bölmektense . lardan bölmeye başlar buraya . , ? gibi şeylerin gelmesi mümkündür
print(okul.split())
# böldüğümüz ve listeye dönüşen ifadeleri birleştirelim
words = okul.split()
print(words)
print(" ".join(words))
# ortalayıp çıktı verme
print("ismail".center(25))


















































































































































































































































































