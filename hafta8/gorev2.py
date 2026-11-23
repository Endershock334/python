# GÖREV 02 | Süper Güç Hesaplayıcısı





# Hesaplama Kuralı:
# Toplam Güç = (Saldırı × 2) + Savunma + Bonus

# B. SİZDEN BEKLENENLER
# Saldırı ve savunma parametrelerini kullan.
# Bonus parametresinin varsayılan değeri 0 olsun.
# Hesaplanan sonucu geri döndür.


def guc_hesapla(saldiri, savunma, bonus=0):
    toplam_guc = (saldiri * 2) + savunma + bonus
    return toplam_guc

sonuc = guc_hesapla(50, 30, 10)
print("Toplam Güç:", sonuc)
