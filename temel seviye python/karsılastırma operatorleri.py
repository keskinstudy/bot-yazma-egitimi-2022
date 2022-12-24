"""
KARŞILAŞTIRMA OPERATÖRLERİ
//////////////////////////////////////////////////////////////////////////////
Python'da değişkenlerin içindeki verileri karşılaştırmak için kullanırız
+----------+----------------+-----------+
| Operatör | Açıklama       | Kullanımı |
+----------+----------------+-----------+
|    ==    | eşit mi?       |   x == y  |
+----------+----------------+-----------+
|    !=    | eşit değil mi? |   x != y  |
+----------+----------------+-----------+
|     >    | büyük mü?      |   x > y   |
+----------+----------------+-----------+
|     <    | küçük mü?      |   x < y   |
+----------+----------------+-----------+
|    >=    | büyük eşit mi? |   x >= y  |
+----------+----------------+-----------+
|    <=    | küçük eşit mi? |   x <= y  |
+----------+----------------+-----------+
"""


# veri tabanı
kullanici_adi = "ismail"
sifre = "senbenibilemedinyuregimigoremedin"

# kullanıcıdan "kullanıcı adı" ve "sifre" bilgilerini alalım ve veritabanını temsil eden değişkenler içindeki veri ile esitliğini kontrol edelim


k_adı = input("kullanıcı adınızı yazınız:")
k_sifre = input("sifrenizi yazınız:")
print(f"kullanıcı adı dogrumu adı: {kullanici_adi == k_adı}")
print(f"sifre doğrumu:{sifre == k_sifre}")

# kullanıcıdan sayı alalım birbirine eşit değil mi diye bakalım

sayı1 = int(input("1.sayıyı girin"))
sayı2 = int(input("2. sayıyı girin"))
print(f"eşit değil mi: {sayı1 != sayı2}")

# iki kişinin yaşını karşılaştıralım
yas1 = 36
yas2 = 25
print(yas1 > yas2)
print(yas1 < yas2)


























































