 # boş bir liste tanımlayalım
liste = []
print(type(liste))

okul = "Sancaktepe Teknoloji Anadolu İmam Hatip Lisesi"
words =  okul.split()
print(words)
# belirli sıradaki kelimeleri yazdıralım
print(words[0])
print(words[1])
print(words[2])
print(words[3])
print(words[4])
print(words[5])
print(words[-1]) # son kelimeyi yazar

ad = "İsmail Hakkı Keskin"
print(ad[0])
print(ad[7:12])

print(ad[7:12:2]) # 1 harfi alır 1 harfi almaz
print(ad[::-1]) # tersten yazar
#  listeler içerisinde farklı türden veriler olabilir
liste = [1,12.31,"python", True , [1,2,3]]
print(liste[-1][-1])
print(liste[4][-1])
# iki listeyi birleştirme
liste_2 = [1,2,3]
liste_3 = [4,5,6]
liste_4 = liste_2+liste_3
liste_5 = liste_3+liste_2
print(liste_4)
print(liste_5)




















































