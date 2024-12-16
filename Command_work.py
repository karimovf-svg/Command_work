class User:
    def __init__(self,phone,carta,password,is_admin,is_client):
        self.phone= phone
        self.carta= carta
        self.korzinka= []
        self.password= password
        self.admin= is_admin
        self.client= is_client

class Maxsulotlar:
    def __init__(self,nomi,narx,muddati):
        self.nomi= nomi
        self.narx= narx
        self.muddati= muddati
        self.soni= 100

class Market:
    def __init__(self,title,baza,balans):
        self.title=title
        self.baza=baza
        self.balans=balans
        self.history=[]