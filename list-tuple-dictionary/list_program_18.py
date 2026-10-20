# List Program 18
mixed = ["apple", 10, "ball", 25, "cat", 7]
# with list comprehension
ints = [x for x in mixed if type(x) == int]
print(ints)
# without list comprehension
for x in mixed:
    if type(x) == int:
        print(x)
