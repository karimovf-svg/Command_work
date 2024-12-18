from  Market import Market
from Users import User
from Tovarlar import Maxsulotlar, data_tovar

while True:
    print("===Uzum Marketga Xush kelibsiz===")
    print("1.Mahsulotlar Ro'yhati")
    print("2.Korzinka")
    print("3.Chiqish")
    status = input("Tanlovni kiriting: ")

    if status == "1":
        data_tovar()

    elif status == "2":
        pass
    elif status == "3":
        break
