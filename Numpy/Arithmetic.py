import numpy as np

# Scalar arithmetic

array = np.array([1, 2, 3])

print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

# Vectorized math funcs

array1 = np.array([1.01, 2.5, 3.99])

print(np.sqrt(array1))

#Nếu phần thập phân là lớn hơn 0.5, nó sẽ làm tròn lên.
#Nếu phần thập phân là nhỏ hơn 0.5, nó sẽ làm tròn xuống.
#Nếu phần thập phân chính xác bằng 0.5, nó sẽ làm tròn đến số chẵn gần nhất. Quy tắc này được gọi là "làm tròn đến số chẵn gần nhất" (round half to even).
print(np.round(array1))
print(np.floor(array1))
print(np.ceil(array1))
print(np.pi)

# Element-wise arithmetic

array2 = np.array([1, 2, 3])
array3 = np.array([4, 5, 6])

print(array2 + array3)
print(array2 - array3)
print(array2 * array3)
print(array2 / array3)
print(array2 ** array3)

# Comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100)
print(scores >= 60)

scores[scores < 60] = 0
print(scores)