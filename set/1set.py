# Exercise 1: Add a list of elements to a set

# Given:
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]

# Expected output:
# {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

new_set = sample_set.union(set(sample_list))

print(new_set)