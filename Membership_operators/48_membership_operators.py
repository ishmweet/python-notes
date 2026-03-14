students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students: # if we use not in then the statements are switched
    print(f"{student} is a student.")
else:
    print(f"{student} was not found.")