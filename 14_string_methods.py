name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

#result = len(name) # displays the length of a string
#result = name.find("o") # searches from left to right
#result = name.rfind("o") # searches from right to left
#name = name.capitalize()
#name = name.upper() # for upper case
#name = name.lower() # for lower case
#result = name.isdigit() # checks if the string contains only digits
#result = name.isalpha() # checks if the string contains only alphabetical characters
#result = phone_number.count("-")
phone_number = phone_number.replace(" ", "")

print(phone_number)