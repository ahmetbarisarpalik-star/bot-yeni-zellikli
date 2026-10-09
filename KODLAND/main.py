import random

def sifre_olustur():
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    sifre = ""

    # Karakter değişkeninden rastgele bir karakter seçmek ve bunu oluşturulan parolanın bulunduğu değişkene eklemek için bir döngü ve random kütüphanesi kullanın
    for i in range(10):
        rastgele_karakter = random.choice(karakterler)
        sifre = sifre + rastgele_karakter
    return sifre
