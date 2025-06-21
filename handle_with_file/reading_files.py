# Python reading files (.txt, .json, .csv)

import csv

file_path = "stuff/output.csv"



try:
    with open(file=file_path,mode="r") as file:
        # content = file.read() .txt

        # content = json.load(file)
        # print(content['age'])

        content = csv.reader(file)
        for line in content:
            print(line[2])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")