# Python writing files (.txt, .json, .csv)
import csv
import json

# .json
# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "stuff/output.csv"


try:
    with open(file=file_path,mode="w", newline="") as file: # with (can help u with closing file)
        # json.dump(employee, file, indent=4)   .json

        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)

        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
# "w": write a file
# "x": likes "w" if file doesn't exist (else error)
# "a": append a file
# "r": read a file