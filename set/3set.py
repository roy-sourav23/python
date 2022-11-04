# Exercise 3: Get Only unique items from two sets

# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# Expected output:
# {70, 40, 10, 50, 20, 60, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

new_set = set1.union(set2)
print(new_set)