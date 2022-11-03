# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# Expected Output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = []
for x in range(len(list1)):
    for y in range(len(list2)):
        list3.append(list1[x]+" "+list2[y])

print(list3)

