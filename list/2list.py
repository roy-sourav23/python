# Exercise 2: Concatenate two lists index-wise

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = []
for x in range(len(list1)):
    list3.append(str(list1[x])+str(list2[x]))

print(list3)