# Tuple = ()
# Tuples are ordered, immutable (unchangeable), and allow duplicate values.
# Tuples are generally faster than lists because they cannot be modified.
# Tuples is the most secure datatype.

fruits = ("apple", "orange", "banana", "coconut")


# Memory allocation
# Python stores the tuple in memory and the variable holds
# the reference (address) of that tuple.

# id() is used to check the memory address
# print(id(fruits))


# Checking if an element exists in the tuple
# print("apple" in fruits)   # returns True if apple exists


# Length of the tuple
# print(len(fruits))


# dir() shows all available tuple methods
# print(dir(fruits))


# index() returns the position of an element
# print(fruits.index("apple"))


# count() counts how many times a value appears
# print(fruits.count("apple"))


# Accessing elements using indexing
# print(fruits[0])    # first element
# print(fruits[-1])   # last element


# Slicing
# print(fruits[1:3])


# Looping through the tuple
# for fruit in fruits:
#     print(fruit)


# Nested tuple example
# nested_tuple = ("apple", ("banana", "mango"), "orange")


# Converting tuple to list if modification is required
# fruits_list = list(fruits)
# fruits_list.append("pineapple")
# fruits = tuple(fruits_list)


print(fruits)


# Important notes

# Tuples maintain insertion order.
# Tuples allow duplicate values.
# Tuples are immutable (values cannot be changed after creation).
# Tuples use parentheses ().
# Tuples can store multiple data types.

# Example of mixed datatype tuple
# mixed_tuple = ("apple", 10, True, 3.14)

# Memory allocation notes

# When a tuple is created, Python allocates memory for the entire tuple.
# Since tuples are immutable, Python does not need to reallocate memory
# when accessing elements, which makes tuples slightly faster than lists.

# Example:
# coordinates = (10, 20)
# Often used for fixed data such as coordinates or RGB values.