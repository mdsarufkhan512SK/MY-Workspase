#29 no video = Python Matrix
saruflist = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    11
]
saruflist[1][3]
print(saruflist[1][3])

#30 no video = Python Tuple Data 

saruftuple = (1,2,3,4,5,6)
print(saruftuple[3])
print(saruftuple[-2])
print(saruftuple[2:4])

#31 no video = Python Update Tuple = 
# tuple k prothom a list 
#koray tarpor a change koray 
# abar tuple kora hoyaca 
saruftuple = ("saruf","se","taiyaba","babuni")
print(type(saruftuple))
se = list(saruftuple)
print(type(se))
se.append("love")
saruftuple = tuple(se)
print(saruftuple)

#33 no videos = Python loop Tuple 
saruftuple = ("saruf","maruf","rafia","abusayad")
for i in saruftuple:
    print(i)
for x in range(len(saruftuple)):
    print(saruftuple[x])
saruftuple = ("saruf","maruf","rafia","abusayad")
y = 0
while y < len(saruftuple):
    print(saruftuple[y])
    y = y + 1

#34 no video = Python Join Tuple 
tuple1 = ("saruf","maruf","rafia")
tuple2 = (1,2,3,4,5,6)
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple1 * 2)
print(tuple2 * 4)

#35 no video = Python Tuple Method 
mytuple = ("saruf","maruf","rafia")
x = mytuple.index("saruf")
print(x)

num_tuple = (1,4,2,4,3,4,5,6)
y = num_tuple.count(4)
print(y)