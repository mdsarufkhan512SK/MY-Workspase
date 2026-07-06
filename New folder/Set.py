#37 no videos = set type data
Myset = {1,2,3,4,5,5,6,6,7,8,1} 
print(Myset)
print(type(Myset))
print(len(Myset))
#38 no videos = Python Access Set Item 
myset = {'apple',"banana","cherry"}
for i in myset:
    print(i)

myset = {'apple',"banana","cherry"}
print("mango" in myset )

#39 no videos =  Python Add Set Item 
Ourset = {"Saruf","maruf","Rafia"}
Ourset.add("jihad")
print(Ourset)

Ourset = {"Saruf","Maruf","Rafia"}
Ourlist = ["Abbu","Ammu","bon","bhai"]
Ourset.update(Ourlist)
print(Ourset)

#40 no videos =  Python Remove Set Item 
Ourset = {"Saruf","Maruf","Rafia","Taiyaba"}
Ourset.remove("Taiyaba")
print(Ourset)

Ourset = {"Saruf","Maruf","Rafia"}
Ourset.discard("Taiyaba")
print(Ourset)

#41 no videos = loop sets
Ourset = {"Saruf","Maruf","Rafia","Abusayad"}
for i in Ourset:
    print(i)


#42 no videos =  Python Join Set
set1 = {'a','b','c'}
set2 = {1,2,3,4}
set1.update(set2)
print(set1)

set1 = {'a','b','c'}
set2 = {1,2,3,4}
set3 = set1.union(set2)
print(set3)



#42.2 Python Set Item Exercise
