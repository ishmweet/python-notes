# List = []
# Lists are ordered, mutable (changeable), and allow duplicate values.

fruits = ["apple", "orange", "banana", "coconut"]

# dir() -> shows all available list methods
# print(dir(fruits))

# len() -> returns number of elements in the list
# print(len(fruits))

# slicing -> used to reverse the list
# print(fruits[::-1])

# membership operator
# print("apple" in fruits)

# Lists are mutable so values can be changed
# fruits[0] = "ok"   # replaces "apple" with "ok"


# List methods

# append() -> adds element at the end
# fruits.append("pineapple")

# remove() -> removes a specific value
# fruits.remove("apple")

# insert() -> inserts element at a specific position
# fruits.insert(0, "pineapple")

# pop() -> removes element using index (default removes last element)
# fruits.pop()
# fruits.pop(1)

# sort() -> sorts list in alphabetical order
# fruits.sort()

# reverse() -> reverses the list order
# fruits.reverse()

# clear() -> removes all elements from the list
# fruits.clear()

# index() -> returns position of a specific element
# print(fruits.index("apple"))

# count() -> counts how many times a value appears
print(fruits.count("apple"))

print(fruits)


# Looping through the list
# for fruit in fruits:
#     print(fruit)


# Important information about lists

# Lists maintain insertion order.
# Lists allow duplicate values.
# Lists are mutable (values can be modified).
# Lists can store different data types.

# Example of mixed data types
# mixed = ["apple", 10, True, 3.14]

# Indexing
# print(fruits[0])    # first element
# print(fruits[-1])   # last element

# Slicing
# print(fruits[1:3])