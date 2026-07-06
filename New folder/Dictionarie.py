#43 Python Dictionaries
Studentdata = {
    "Saruf":{
        "Name":"MD_Saruf_Khan",
        "Age":"19+",
       "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227603",
        "Semester":"3rd",
        "phone":"01000000082",


    },
    "Sohan":{
        "Name":"MD_Sohan_Shake",
        "Age":"19+",
        "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227600",
        "Semester":"3rd",
        "phone":"01000000000",

    },
    "Code":"Python",

    
}
print(Studentdata["Saruf"]["Name"])


print(Studentdata["Sohan"]["College"])


#44 Python Dictionaries Access 

Studentdata = {
    "Saruf":{
        "Name":"MD_Saruf_Khan",
        "Age":"19+",
       "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227603",
        "Samister":"3rd",
        "phone":"01000000082",


    },
    "Sohan":{
        "Name":"MD_Sohan_Shake",
        "Age":"19+",
        "Collage":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227600",
        "Samister":"3rd",
        "phone":"01000000000",

    },
    "Code":"Python",

    
}

print(Studentdata["Code"])

x = Studentdata.get("Saruf")
print(x)

y = Studentdata.keys()
print(y)

z = Studentdata.values()
print(z)

#45 Python Dictionaries Change Item
Studentdata = {
    "Saruf":{
        "Name":"MD_Saruf_Khan",
        "Age":"19+",
       "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227603",
        "Semester":"3rd",
        "phone":"01000000082",


    },
    "Sohan":{
        "Name":"MD_Sohan_Shake",
        "Age":"19+",
        "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227600",
        "Semester":"3rd",
        "phone":"01000000000",

    },
    "Code":"Python",

    
}

Studentdata["Code"] = ["Coding"]
print(Studentdata["Code"])

Studentdata.update({"Sohan":"Sohan is a Student at Khulna Polytechnic Institute."})
print(Studentdata["Sohan"])

#46 Python Dictionaries = Remove item 


Studentdata = {
    "Saruf":{
        "Name":"MD_Saruf_Khan",
        "Age":"19+",
       "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227603",
        "Semester":"3rd",
        "phone":"01000000082",


    },
    "Sohan":{
        "Name":"MD_Sohan_Shake",
        "Age":"19+",
        "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227600",
        "Semester":"3rd",
        "phone":"01000000000",

    },
    "Code":"Python",

    
}

Studentdata.pop("Sohan")
print(Studentdata)
Studentdata.popitem()
print(Studentdata)
del Studentdata ["Saruf"]
print(Studentdata)


Studentdata = {
    "Saruf":{
        "Name":"MD_Saruf_Khan",
        "Age":"19+",
       "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227603",
        "Semester":"3rd",
        "phone":"01000000082",


    },
    "Sohan":{
        "Name":"MD_Sohan_Shake",
        "Age":"19+",
        "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227600",
        "Semester":"3rd",
        "phone":"01000000000",

    },
    "Code":"Python",

    
}

Studentdata.clear()
print(Studentdata)



#47 Python Loop Dictionary 

Studentdata = {
    "Saruf":{
        "Name":"MD_Saruf_Khan",
        "Age":"19+",
       "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227603",
        "Semester":"3rd",
        "phone":"01000000082",


    },
    "Sohan":{
        "Name":"MD_Sohan_Shake",
        "Age":"19+",
        "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227600",
        "Semester":"3rd",
        "phone":"01000000000",

    },
    "Code":"Python",

    
}

for i in Studentdata:
    print(i)


for x in Studentdata.values():
  print(x)

for x in Studentdata.keys():
    print(x)

for y in Studentdata.items():
    print(y)


#47.2 Python Copy Dictionary
Studentdata = {
    "Saruf":{
        "Name":"MD_Saruf_Khan",
        "Age":"19+",
       "College":"Khulna Polytechnic Institute",
        "Dep":"C.S.T",
        "Roll":"227603",
        "Semester":"3rd",
        "phone":"01000000082",
},
} 

print(Studentdata)


Studentdata.copy()

print(Studentdata)

x = dict(Studentdata)
print(x)




#48 Python Dictionary Exercises

#Exercises is compleated 



