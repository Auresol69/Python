import numpy as np

array = np.array([[['A','B','C'], ['D','E','F'], ['G','H','I']],
                  [['J','K','L'], ['M','N','O'], ['P','Q','R']],
                  [['S','T','U'], ['V','W','X'], ['Y','Z','_']]])

print(array.ndim)

print(array.shape) # (3,    3,    3)
                  # Depth  Row  Column

# Chain indexing
# print(array[1][2][0]) # P

# Multi-dimensional indexing ( faster than chain indexing for sure :D )
print(array[1,2,0])

# More exercises

word = array[0,0,0] + array[2,0,0] + array[2,0,0]

print(word)