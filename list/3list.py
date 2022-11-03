# Exercise 3: Turn every item of a list into its square

list = [1, 2, 3]

def list_square(list):
    new_list = []
    for x in range(len(list)):
        new_list.append(list[x]**2)
    return new_list

squared_list = list_square(list)
print(squared_list)
