# kullanıcıdan 2 sayı alıp toplama işlemi yapan program
# sayi1 = input("1. sayıyı giriniz :")
# sayi2 = input("2. sayıyı giriniz :")
# print(float(sayi1)+float(sayi2))
# exit("tamamlandı")
# basit hesap makinesi

# farklı veri tiplerine bakalım : type()
x = 1 # int
y = 1.2 # float
ad = "ismail" #string
sinav_basarili_mi = True # boolean
print(type(x))
print(type(y))
print(type(ad))
print(type(sinav_basarili_mi))

# tip dönüştürme
# intten floata
print(float(x))

# floattan inte
print(int(y))

# booldan stringe
print(str(sinav_basarili_mi)) # metne dönüştürdü (metin olarak true yazıcak eğer çalıştırırsak.Düz bir şekilde bool olarak yazarsak metin olarak yazılmayacak)

# booldan inte
print(int(sinav_basarili_mi))

# intten stringe
print(str(x)) # booldan strinngede olan şey ile aynı

# stringden inte
#print(int(ad)) # metinler inte dönüşmez

sayi = "36"
print(int(sayi)) # sayı değeri taşıyan string dönüşebilir

















