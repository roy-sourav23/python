# Exercise 4: Initialize dictionary with default values

# Given:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# Expected Output:
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 
#  'Emma': {'designation': 'Developer', 'salary': 8000}
# }

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# The fromkeys() method returns a dictionary with the specified keys and the specified value.
dict1 = dict.fromkeys(employees, defaults)
print(dict1)