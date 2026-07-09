class mess_friend:
    def __init__(self,Name,Age):
        self.__Name = Name   # private variable
        self.Age = Age  #public Variable
        print(self.__Name)



M1 = mess_friend("Khalukul",19)
print(M1.Age)


print(M1.Name)  # ata error dibay kron ata baher thakay accse naowahar chata kortayca 



# __   aita manay holo kno kicu kl private kora jatay kaow bairay thakay accase na kortay paray , ata funcation method variable j kono jaygay use korajay


# __ ata sudu class ba jeta or range oi ar bahere accese kora jaby na 