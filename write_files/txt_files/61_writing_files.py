employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "write_files/txt_files/employee_output.txt"

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created.")
except FileExistsError:
    print("That file already exists.")