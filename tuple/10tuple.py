# Exercise 10: Check if all items in the tuple are the same

# tuple1 = (45, 45, 45, 45)

# Expected output:
# True

tuple1 = (45, 45, 45, 45)

def check_same(my_tuple) -> bool:
    return len(my_tuple) == my_tuple.count(my_tuple[0])

print(check_same(tuple1))