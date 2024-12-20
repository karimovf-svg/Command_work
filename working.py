"""Azamat"""
from users import users
from market import market
from mahsulotlar import tavarlar


def work():
    is_user = int(input("Telefon raqam kiriting: "))
    password = int(input("Parolingizni kiriting: "))
    for user in users:
        if is_user == user.phone and password == user.password:
            while True:
                status = input(f"{market.title}ga xush kelibsiz!"
                               f"\nMahsulotlarni ko`rish: 1 \nKorzinkani ko`rish: 2 \nChiqish: 0 ")
                if status == "0":
                    break
                if status == "1":
                    for item in tavarlar:
                        print(f"Mahsulot nomi: {item.nomi}, narxi: {item.narx}")
                    mahsulot = input("Mahsulot nomini kiriting: ")
                    miqdori = int(input("Miqdorini kiriting: "))
                    for item in tavarlar:
                        if mahsulot==item.nomi:
                            print(f"{miqdori} ta {item.nomi} mahsuloti {item.narx * miqdori} so`m bo`ldi.")
                            user.korzina.append(mahsulot)
                if status == "2":
                    for i in user.korzina:
                        print(i)

        else:
            print("Telefon raqam topilmadi yoki parol noto`g`ri!")
            break



work()
