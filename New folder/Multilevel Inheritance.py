
#61 Python Multilevel Inheritance
class baba:
    car = "BMW"
    Home = "30 floor"
    taka = "50 Milion"
    Jayga = "500 biga"

class son1(baba):
    House = "3 floor"
    garaze = "2 ta"
    jayga = "100 biga"

class son2(son1):
    bari = "1 floor"
    garage = "1 ta"
    gari = "15 ta"

class son3(son2):
    Shop = "1 ta"
    gari = "1 ta"
    jayga = "10 sotok"

class son4(son3):
    car_nei = ""
    bari_banga = ""

s1= son1
s2 = son2
s3 = son3
s4 = son4
print(s1.car)
print(s2.garage)
print(s3.House)
print(s4.bari)
print(baba.Jayga)



