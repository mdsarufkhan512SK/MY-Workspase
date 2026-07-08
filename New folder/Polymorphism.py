class Friendname:
    def __init__(self,Name,Age,Roll,Dep):
    self.Name = Name
    self.Age = Age 
    self.Roll = Roll
    self.Dep = Dep



class Sohan(Friendname):
    pass
class Abir(Friendname):
    pass
class Nur(Friendname):
    pass
class Aditto(Friendname):
    pass
class Habibur(Friendname):
    pass



S = Sohan("Sohan",19,"227***","CST")
A = Abir("Abir","19","227600","CST")
N = Nur("Nur",19,"227***","CST")
Ad = Aditto("Aditto",19,"2276**","CST")
H = Habibur("Habibur","19","227***","CST")


print(S.Name,S.Age,S.Roll,S.Dep)
print(A.Name,A.Age,A.Roll,A.Dep)
print(N.Name,N.Age,N.Roll,N.Dep)
print(Ad.Name,Ad.Age,Ad.Roll,Ad.Dep)
print(H.Name,H.Age,H.Roll,H.Dep)