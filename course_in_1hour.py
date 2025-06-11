# Variable = A container for a value (String, integer, float, boolean)
#            A variable behaves as if it was the value it contains
import math

#String
first_name = "Roy"

print(f"Hello {first_name}") # f for formatting, use for all type variables

print(type(first_name)) # type() for show type variables

first_name = bool(first_name) # you can check if the first_name is empty (first_name = "")

print(first_name)

#Integer
age = 25

age = str(age)
age += "1"

print(age)

#Float
price = 10.99

price = int(price) # type variable() for type cast

print(price)

#Boolean
is_student = False

if  is_student:
    print("You are a student")
else:
    print("You are NOT a student")

#math

# result = round(x,INDEX) lam tron, INDEX la so thap phan muon lam tron
# result = abs(y) gia tri tuyet doi
# result = pow(4,3) tuong tu nhu **3, con duoc goi la mu~ 3
# result = max(x,y,z) tim max
# result = min(x,y,z) tim min

import course_in_1hour

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x) lam tron LEN
# result = math.floor(x) lam tron XUONG

# example
radius = float(input("Nhap: "))
area = math.pi * pow(radius,2)
print(f"Dien tich hinh tron la: {round(area,3)}")

# cau dieu kien if
age = int(input("Enter your age: "))

if age >=100:
    print("You are an old man")
elif age >=18:
    print("You are an adult")
elif age <0:
    print("You are not born yet")
else:
    print("You are a child")

