import json

file_path = "write_files/json_files/j_output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["age"])
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to read that file.")
    