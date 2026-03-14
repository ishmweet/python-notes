# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You didn't enter your name.")
    name = input("Enter your name: ")

    print(f"Hello {name}")