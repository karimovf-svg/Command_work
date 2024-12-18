"""Muhammadaziz"""
class Maxsulotlar:
    def __init__(self,nomi,muddati,narx):
        self.nomi= nomi
        self.narx= narx
        self.muddati= muddati
        self.soni= 100
def data_tovar():
    maxsulot1 = Maxsulotlar("Piyoz:", "1-yil", 10)
    maxsulot2 = Maxsulotlar("Sabzi:", "1-yil", 10)
    maxsulot3 = Maxsulotlar("Kartoshka:", "1-yil", 10)
    maxsulot4 = Maxsulotlar("Bodiring:", "1-hafta", 25)
    maxsulot5 = Maxsulotlar("Pomidor:", "1-hafta", 25)
    maxsulot6 = Maxsulotlar("Chisnok:", "1-yil", 5)
    maxsulot7 = Maxsulotlar("Non:", "1-hafta", 5)
    maxsulot8 = Maxsulotlar("Go'sht:", "1-hafta", 90)
    maxsulot9 = Maxsulotlar("Tuxum:", "1-oy", 30)
    maxsulot10 = Maxsulotlar("Dubayskiy chocolate:", "3-oy", 200)

    baza = [maxsulot1, maxsulot2, maxsulot3, maxsulot4, maxsulot5, maxsulot6, maxsulot7, maxsulot8, maxsulot9,maxsulot10]
    print("===Mahsulotlar===")
    for maxsulot in baza:
        print(f"\nNomi:{maxsulot.nomi} \nMuddati:{maxsulot.muddati} \nNarxi:{maxsulot.narx}$")