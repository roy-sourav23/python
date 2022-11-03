# Exercise 6: Delete a list of keys from a dictionary

# Given:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# Keys to remove
# keys = ["name", "salary"]

# Expected output:
# {'city': 'New york', 'age': 25}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

for i in range(len(keys)):
    if keys[i] in sample_dict.keys():
        sample_dict.pop(keys[i])

print(sample_dict)

