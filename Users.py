class User:
    def __init__(self,phone,carta,password,is_admin,is_client):
        self.phone= phone
        self.carta= carta
        self.korzinka= []
        self.password= password
        self.admin= is_admin
        self.client= is_client

user1 = User("+998902040737", 4023561498601122, 1111,False,True)
user2 = User("+998902020582", 4023561498602222, 2222,False,True)
user3 = User("+998889931022", 4023561498603322, 3333,False,True)
user4 = User("+998999069999", 4023561498604422, 4444,False,True)
user5 = User("+998999060582",9999,7777,True,False)