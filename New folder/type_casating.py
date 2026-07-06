#17 no videwo = type casting 
num = "57"
print(float(num))
print(int(num))
#18 no videos  = list 
li =  [1,2,3,43,4,5]
li[3] = 4
print(li)
lis = [2,3,4,5]
lis[2] = 45
print(lis)
list = [56,456,76,3]
list[2] = 53
print(list)
#19 no videos = change list items
li = ['Youtube cnannel','facebook page','instagram page']
print(li[2])
li[2] = 'tiktok id'
print(li)
#20 no videos = Add list items
li.append("linkdin id")
print(li)
li.insert(1, 100)
print(li)
#21 no video = remove in list items
newlist = ["rafia","saruf","maruf","abusayad"]
#newlist.remove("maruf")
#print(newlist)
#newlist.pop(0)
#print(newlist)
#del newlist[0]
#print(newlist)
newlist.clear()
print(newlist)
####22 no videos = loop list
#for loop  
name = ["saruf","maruf","rafia","abusayad"]
for prem in name:
    print(prem)
for i in range(len(name)):
    print(i)
#while loop
y = 0
while y < len(name):
    print(name[y])
    y = y + 1
#23 no videos = List Comprehension 
saruf = [1,2,3,4,5,6,7,8,9,10]
se = [i * 2 for i in saruf]
print(se)
###24 no videos = Sort List 
saruf = [32,54,23,566,1,2,3,4,45,57,34,34]
se = ["a","b","d","t","y","s","e"]
a = ["saruf","rafia","jihad","maruf"]
a.sort()
se.sort()
saruf.sort()
print(saruf)
print(se)
print(a)
#reverse
saruf = [1,2,3,4,5,6,7,8,9,10]
saruf.sort(reverse = True)
print(saruf)
###25 no videos = Copy A List
saruf = [1,2,3,4,5,6,7,8,9,10]
se = saruf.copy()
print(saruf)
print(se)
####26 no videos = join tow list
saruf = [1,2,3,4,5]
se = [6,7,8,9,10]
plass = saruf + se
print(plass)
saruf.extend(se)
print(saruf)
