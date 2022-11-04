# Exercise 4: Update the first set with items that don’t exist in the second set

# Given:
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}

# Expected output:
# set1 {10, 30}

set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1 = set1.difference(set2)
print(f"set1 {set1}")