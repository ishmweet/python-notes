txt_data = "I like pizza"

file_path = "write_files/txt_files/t_output.txt"

try:
    with open(file_path, "x") as file:  # exclusive create mode: creates new file but errors if it already exists
        file.write(txt_data)
        print(f"txt file '{file_path}' was created.")
except FileExistsError:
    print("That file already exists.")