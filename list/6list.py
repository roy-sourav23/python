# Exercise 6: Remove empty strings from the list of strings

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:

# ["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
n_list = []
for x in range(len(list1)):
    if len(list1[x]) > 0:
        n_list.append(list1[x])

print(n_list)