#Use the correct syntax to print the number of items in the fruits tuple.

fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(
fruits[0])

#Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

mytuple = ("apple", "banana", "hasdio")

# Deletes the entire tuple variable
del mytuple

# This will cause a NameError because 'mytuple' no longer exists
try:
    print(mytuple)
except NameError:
    print("Error: mytuple does not exist anymore!")
