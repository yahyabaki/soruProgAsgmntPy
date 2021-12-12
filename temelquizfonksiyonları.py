from SoruSınıfı import Sorular

#Alt kısım soru dosyasından çekilecek, şimdilik referans olarak bulunmakta
"""
SoruTanımları = [
    "Eiffel Kulesi Paris'te midir? \n(a)evet \n(b)hayır \n\n",
    "Giza Piramitleri Çin'de midir? \n(a)evet \n(b)hayır \n\n"
]
a = Sorular(SoruTanımları[0], "a") ;b = Sorular(SoruTanımları[1], "b")
SoruCevap = [a,b]
"""
def testiBaşlat(soruListesi):
    skor = 0
    for i in soruListesi:
        cevap = input(i.soru)
        if cevap == i.cevap:
            skor += 1
    print("sorulardan " + str(skor) + "/" + str(len(soruListesi)) + "'unu/ini doğru cevapladınız.")
testiBaşlat("""SoruCevap(yorum içinde tanımlı)""")