name = input("Enter ur name: ")

while not name.isalpha() or not name:
    print("U did not enter ur name!!")
    name = input("Enter ur name: ")
else:
    print(f"Hello {name}")