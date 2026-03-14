email = input("Enter your email: ")

if "@" in email and "." in email:
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is an invalid email address.")