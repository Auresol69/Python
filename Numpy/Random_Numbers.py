import numpy as np

# Random number generator
rng = np.random.default_rng(seed=4)

print(rng.integers(low=1, high=101,size=(3,2)))

np.random.seed(seed=1)

print(np.random.uniform(low=-1, high=1, size=(3, 2)))

rng1 = np.random.default_rng()

array = np.array([1, 2, 3, 4, 5])
rng1.shuffle(array)

print(array)

rng = np.random.default_rng()

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
fruit = rng.choice(fruits, size=(3, 3))
print(fruit)

