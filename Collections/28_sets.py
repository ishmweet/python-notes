# Set = {}
# Sets are unordered and do not allow duplicate values.
# Sets are mutable (elements can be added or removed),
# but the elements themselves must be immutable.

fruits = {"apple", "orange", "banana", "coconut"}


# Sets do NOT support indexing because they are unordered
# fruits[0] = "ok"   # This will cause an error


# dir() -> shows all available set methods
# print(dir(fruits))


# len() -> returns number of elements in the set
# print(len(fruits))


# Membership operator
# print("apple" in fruits)   # checks if apple exists in the set


# Adding elements
# fruits.add("pineapple")


# Removing elements
# fruits.remove("apple")   # removes apple (error if not found)


# discard() -> removes element without error if not found
# fruits.discard("apple")


# pop() -> removes a random element (since sets are unordered)
# fruits.pop()


# clear() -> removes all elements from the set
# fruits.clear()


# Looping through a set
# for fruit in fruits:
#     print(fruit)


print(fruits)


# Important notes

# Sets do not maintain insertion order.
# Sets do not allow duplicate values.
# Sets do not support indexing or slicing.
# Sets are mutable, so elements can be added or removed.
# Sets use curly braces {}.

# Example of duplicates (duplicates are automatically removed)
# numbers = {1, 2, 2, 3, 3, 4}
# print(numbers)   # output will be {1, 2, 3, 4}


# Sets can store multiple immutable data types
# example = {"apple", 10, True}


# Memory concept
# Python allocates memory for the entire set object,
# and the variable holds a reference to that memory location.

# print(id(fruits))