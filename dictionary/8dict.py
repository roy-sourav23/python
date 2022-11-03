# Exercise 8: Rename key of a dictionary

# Given:
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# Expected output:
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

def rename_key(dict1, old_key, new_key):
    if old_key in dict1.keys():
        dict1[new_key] = dict1[old_key] # new key takes the value of old key
        dict1.pop(old_key)  # old key deleted

rename_key(sample_dict, "city", "location")
print(sample_dict)