#42.2 Python Set Item Exercise

#Which one of these is a set?
myset = ('apple', 'banana', 'cherry')
myset = ['apple', 'banana', 'cherry']
myset = {'apple', 'banana', 'cherry'}


#Select the correct function for returning the number of items in a set:
fruits = {'apple', 'banana', 'cherry'}
print(len(fruits))


#Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")


#Use the correct method to add multiple items (more_fruits) to the fruits set.

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)



fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
set1 = fruits.union(more_fruits)
print(set1)



#Use the remove method to remove "banana" from the fruits set.


fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
