"""Muhammadaziz"""
from mahsulotlar import tavarlar


class Market:
    def __init__(self, title, balance):
        self.title = title
        self.baza = []
        self.balance = balance


market = Market("Uzum Market",10000)
market.baza.append(tavarlar)
