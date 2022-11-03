# Exercise 10: Remove all occurrences of a specific item from a list.

# Given:
# list1 = [5, 20, 15, 20, 25, 50, 20]

# Expected output:
# [5, 15, 25, 50]


list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)

print(list1)
