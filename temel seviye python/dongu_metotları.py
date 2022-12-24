# metot: range()
# range() fonkdiyonunu belli bir aralıkta bulunan sayıları
# dondurmek için kullanırız

# 1 - 10 sayıları arasındaki sayılardan olusan bir liste,
liste = list(range(1,10))
print(liste)

# ekrana 50 defa python yazdıralımj
#örnek 1. python
for sayi in range(50):
    print(f"{sayi+1}.python")

# metot: enumate()
# ingilizcede enumarate kelimesi numaralandırmak anlamına gelir
#  fonksiyonun gorevi nesne elemanlarını numaralandırarak dondurmektir

 # python kelimesinin karakterlerini enumee ile numaralandırıp ekrana yazdıralım

kelime = "python"
kelime_enum = list(enumerate(kelime))
print(kelime_enum)

# metot zip()
#zip listeleri birleştirme işlemi yapar
# sayılardan ve o sayıların okunuşlarından oluan 2 liste oluşturalım

sayilar = [1,2,3]
okunuşlar = ["bir","iki","üç"]

# bu sayıları zip ile birleştirelim
sayilar_zip = list(zip(sayilar,okunuşlar))
print(sayilar_zip)

# for döngüsü içinde sayıları ve okunuşları ekrana yazdıralım
for sayi,okunus in zip(sayilar,okunuşlar):
    print(sayi,okunus)



































































