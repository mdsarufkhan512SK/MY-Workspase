#60 Python Multiple Inheritance

class baba:
    car = "BMW"
    Home = "30 floor"
    taka = "50 Milion"
    Jayga = "500 biga"

class kaka1:
    House = "3 floor"
    garaze = "2 ta"
    jayga = "100 biga"

class kaka2:
    bari = "1 floor"
    garage = "1 ta"
    gari = "15 ta"

class kaka3:
    Shop = "1 ta"
    gari = "1 ta"
    jayga = "10 sotok"

class kaka(baba,kaka1,kaka2,kaka3):
    car_nei = ""
    bari_banga = ""

k = kaka
print(k.car)
print(k.garage)
print(k.House)
print(k.bari)
print(k.Jayga)
