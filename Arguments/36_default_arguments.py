# default arguments = A default value of for certain parameters
#                     default is used when that argument is ommited
#                     make your functions more flexible, reduces # of arguments

def greet(name="User"):
    print(f"Hello,{name}")

greet()              # Uses default → "Hello, User"
greet("Dexter")      # Overrides default → "Hello, Dexter"