"""Muhammadaziz"""
class Market:
    def __init__(self,title,baza,balans):
        self.title=title
        self.baza=baza
        self.balans=balans

    def balans_data(self):
        if self.balans >= 0:
            print(f"Market nomi: {self.title}\n Balans: {self.balans}$")
        else:
            print("Market balansida muammo bor, balans manfiy!")

market = Market("Uzum", None, 0)

