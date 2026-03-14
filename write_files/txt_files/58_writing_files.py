# Writing python files (.txt, .json, .csv)

txt_data = "I like pizza"

file_path = "write_files/txt_files/t_output.txt"

with open(file_path, "w") as file:  # write mode: creates file or overwrites existing content from the start
    file.write(txt_data)
    print(f"txt file '{file_path}' was created.")