txt_data = "I like pizza"

file_path = "write_files/txt_files/t_output.txt"

try:
    with open(file_path, "a") as file:  # append mode: creates file if needed and adds new data to the end
        file.write("\n" + txt_data)
        print(f"txt file '{file_path}' was created.")
except FileExistsError:
    print("That file already exists.")