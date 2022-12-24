# Değişkenler olmadan 2 öğrencinin sınav notlarını hesaplayalım
# print((80*0.4) + (75*0.6))
# print((45*0.4) + (60*0.6))

#değişkenlerle 2 öğrencinin sınav notlarını hesaplayalım
sinav1_yuzde = 0.4
sinav2_yuzde = 0.6
# sınav1_yüzde = x
# sınav2_yüzde = y


print( (80*sinav1_yuzde)+(75*sinav2_yuzde) )
print((45*sinav1_yuzde)+(60*sinav2_yuzde))

# DEĞİŞKEN TANIMLAMA KURALLARI

# Rakam ile başlayamaz
# örnek = 1sayı = 85 hatalıdır çünkü rakam ile başlayamaz

# Büuük küçük harfe duyarlıdır
number = 12
NUMBER = 15
print(number)
print(NUMBER)
# ikiside number olmasına rağmen büyük küçük harfe duyarlı olduğundan iki farklı sayı tanımlayabildik

# Türkçe karakter kullanılamaz örnek = ş,ü,ö vb.
# yaş = 18 hatalı kullanım doğru olması için yas = 18 olması lazım ( ancak kelimeleri ingilizce kulanmak daha doğrudur)# s = 18 # Türkçe karakter olmadan türkçe yazmak tavsiye edilmez

#DEĞİŞKENLERDEKİ VERİLERİ BİRLEŞTİRME
x = 1 # int
y = 1.2 # float
ad = "ismail" #string
sinav_basarili_mi = True # boolean

print(x+y)
print(x+sinav_basarili_mi)
# print(ad+sinav_basarili_mi) hata verdi çünkü bool yani boolean ile string toplanamaz
# print(x+ad) hata verdi çünkü int ve string toplanamaz























