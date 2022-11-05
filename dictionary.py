"""
Dictionary "anahtar", "değer" ikililerinden oluşur
    "ad": "ismail"
    "soyad": "keskin"
"""

# belirli bir numaraya sahip öğrenciyi bulma işlemini liste ile yapalım
numaralar = [66,75]
isimler = ["ahmet","mehmet"]
# konum = numaralar.index(numara)
# print(isimler[konum])

# belirli bir numaraya sahip öğrenciyi bulma işlemini dictionary ile yapalım
ogrenciler = {66:"ahmet",75:"mehmet"}

# detaylı örnek
kisiler = {
    1:{
        "ad":"ismail",
        "soyad":"keskin",
        "cinsiyet": True,

    },
    45: {
        "ad":"merve",
        "soyad":"kara",
        "cinsiyet": False,
    }
}
    # 45 numaralı öğrencinin ismini yazdıralım
print(kisiler[45]["ad"])
















































































