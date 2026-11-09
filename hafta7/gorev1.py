# Senaryo: Bir oyun turnuvasında oyuncuların puanlarını saklayan ve en başarılı oyuncuyu belirleyen sistem geliştirilecektir.

# Oyuncuların isimlerini listeye kaydet.
oyuncular = ["Kerem","Ege","Samet","Mert","Berkay"]

# Oyuncuların isimlerini listeye kaydet.
puanlar = [90,80,95,50,100]

# Oyuncuları puanlarıyla birlikte ekrana yazdır.
for i in range(len(puanlar)): 
    print("Sıra Numarası:", i, oyuncular[i], puanlar[i])

# En yüksek puanı alan oyuncuyu belirle.
print("En Yüksek Puan:", max(puanlar), "Kazanan oyuncu:", oyuncular[puanlar.index(max(puanlar))])

# Listeye yeni bir oyuncu ekle.
oyuncular.append("Aras")






