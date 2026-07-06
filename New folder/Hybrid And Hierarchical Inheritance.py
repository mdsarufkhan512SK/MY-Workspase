
#62 Python Hybrid And Hierarchical Inheritance
class Dadu:
    car = "BMW"
    Home = "30 floor"
    taka = "50 Milion"
    Jayga = "500 biga"

class Baba(Dadu):
    House = "3 floor"
    garaze = "2 ta"
    jayga = "100 biga"

class Kaka(Dadu):
    bari = "1 floor"
    garage = "1 ta"
    gari = "15 ta"

class Me(Baba):
    Shop = ""
    gari = ""
    jayga = ""

class Brother(Baba):
    car_nei = ""
    bari_banga = ""

class cousin(Kaka):
    House = ""
    Car = ""

class cousin_2():
    House = ""
    Car = ""
    Shop = ""



B = Baba
K = Kaka
M = Me
B = Brother
C = cousin
c2 = cousin_2

print(B.car)
print(K.garage)
print(M.House)
print(B.House)
print(C.Jayga)
print(c2.Shop)



