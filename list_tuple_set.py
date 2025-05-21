# List [] = mutable, most flexible                       mutable (adj): co the thay doi
# Tuple () = immutable, faster
# Set {} = mutable (add, remove), unordered,             unordered (adj): khong co thu tu
#          No duplicates, best for membership testing

# List []
fruits = ["apple","orange","banana","coconut"]

# print(fruits[3])

# fruits[0] = "pineapple"
# fruits.append("strawberry")
# fruits.remove("orange")
# fruits.pop(1)
# fruits.clear()

print(len(fruits))

for fruit in fruits:
    print(fruit, end=" ")

print()
# Tuple ()
fruits_1 = ("apple","orange","banana","coconut")

for fruit in fruits_1:
    print(fruit, end=" ")
print()
print("Tuple () khong duoc chinh sua")

# Set {}
fruits_2 = {"apple","orange","banana","coconut", "orange"}

# fruits_2.remove("coconut")
# fruits_2.add("lemon")
# fruits_2.clear()

for fruit in fruits_2:
    print(fruit, end=" ")
print()
print("Tuple () khong co thu tu nen khong xai duoc pop, replace va khong lay duoc thu tu gia tri, gia tri khong duoc duplicate")

# co the kiem tra xem co trai cay do khong
fruit = input("Enter a fruit to search for: ")


if fruit in fruits_2:
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not found")