# Exercise 5: Create a dictionary by extracting the keys from a given dictionary

# Given dictionary:

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# Keys to extract
# keys = ["name", "salary"]

# Expected output:

# {'name': 'Kelly', 'salary': 8000}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

dict1 = {}
for x in range(len(keys)):
    if keys[x] in sample_dict:
        dict1[keys[x]] = sample_dict[keys[x]]
print(dict1)