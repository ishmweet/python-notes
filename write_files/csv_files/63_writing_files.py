# csv - comma seperated values

import csv

employees = [["Name", "Age", "Job"],
            ["Spongebob", 30, "Cook"],
            ["Patrick", 37, "Unemployed"],
            ["Sandy", 27, "Scientist"]]

file_path = "write_files/csv_files/csv_output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created.")
except FileExistsError:
    print("That file already exists.")
