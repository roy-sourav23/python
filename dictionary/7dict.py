# Exercise 7: Check if a value exists in a dictionary

# Given:
# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# Expected output:
# 200 present in a dict

sample_dict = {'a': 100, 'b': 200, 'c': 300}

def present_value(dict1, value):
    if value in dict1.values():
        print(f"{value} present in a dict")

present_value(sample_dict, 200)