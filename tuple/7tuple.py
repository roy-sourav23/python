# Exercise 7: Modify the tuple
# Given:
# tuple1 = (11, [22, 33], 44, 55)

# Expected output:
# tuple1: (11, [222, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)

tuple1[1][0] = 222
print(tuple1)

# we can modify a tuple, but can modify a nested list 
# inside a tuple