file_path = "write_files/txt_files/t_output.txt"

try:
    with open(file_path, "r") as file: # r is for reading the content inside files
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to read that file.")
    