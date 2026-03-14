def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

full_name = create_name(first_name, last_name)
print(full_name)