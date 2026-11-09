# Projenin Amacı
# Oyuncunun topladığı eşyaları saklayabileceği, 
# envanterine eşya ekleyebileceği ve eşyalarını kullanabileceği bir sistem geliştirmek.

# Başlangıç envanteri oluştur.
envanter = {
    "Çivi": 114,
    "Paslı Kılıç": 1,
    "Tahta": 540
}

# Oyuncuya seçenekler sun.
print(input("Yerde 5 tane Para var. E ile al:"))

# Envantere eşya ekle.
if input == "E":
    envanter["Para"] = 5

# Envanterdeki eşyaları listele.
print(envanter)

# Eşya kullanımında miktarı azalt.
print(input("Paslı kılıcın kullanılmaz halde. F ile bırak:"))
if input == "F":
    envanter["Paslı Kılıç"] -= 1
print(envanter)

# Oyuncu çıkış yapana kadar programı çalıştır.
    








