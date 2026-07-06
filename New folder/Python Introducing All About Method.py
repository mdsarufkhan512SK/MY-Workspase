class Myclass:

    def Instancemethod(self):
        print("This is Instancemethod")

    @classmethod
    def Classmethod(cls):
        print("This is Classmethod")

    @staticmethod
    def Staticmethod():
        print("This is Staticmathod")

    
Saruf = Myclass()



Saruf.Instancemethod()

Saruf.Classmethod()
Myclass.Classmethod()

Saruf.Staticmethod()
Myclass.Staticmethod()

