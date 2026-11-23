# Oyuncunun mevcut puanına bonus puan ekleyen ve sonucu return ile döndüren bir fonksiyon oluştur.

# ÖRNEK
#def puanlama(puan, carpan):
    #toplam = puan * carpan
    #return toplam # return çağırıldığı yere bilgiyi yollar. çağırıldığı yere toplamı yollicak

#sonuc = 10 * puanlama(10,5) # 50
#print("TAM SONUÇ:", sonuc)


def skor_hesapla(skor, bonus):
    toplam = skor * bonus
    return toplam

sonuc = 10 * skor_hesapla(15, 4)
print("Aldığınız skor :", sonuc)