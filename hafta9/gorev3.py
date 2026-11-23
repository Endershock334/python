# Bir karakterin mevcut canından aldığı hasarı çıkaran hasar_al fonksiyonunu oluştur.
def hasar_al(can, hasar):
    kalan_can = can - hasar
    if kalan_can < 0:
        kalan_can = 0
    return kalan_can

hasar_al(100, 35)

print("Kalan can:", hasar_al(100, 35))




# 2 parametre alcaksınız: can, hasar | Amacımız hasar al fonksiyonunu kullanıp kalan canı ekrana yazdırmak