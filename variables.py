# Variable = A container for a value (String, integer, float, boolean)
#            A variable behaves as if it was the value it contains

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