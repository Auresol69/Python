# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]
danh_sach_so= [1, 2, 3, 4, 5]
binh_phuong_lc= [so * so for so in danh_sach_so]
print(binh_phuong_lc)

doubles = [x * 2 for x in range(1,11)]

fruits = [fruit.upper() for fruit in ["apple","banana","coconut"]]
print(fruits)

fruit_chars = [fruit[0] for fruit in ["apple","banana","coconut"]]
print(fruit_chars)

numbers = [1,2,3,4,5,6,7,8,9]

number_odds= [x for x in numbers if x % 2 == 1]
print(number_odds)