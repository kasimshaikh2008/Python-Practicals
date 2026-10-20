# Program 19: Find common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []
for x in list1:
    if x in list2:
        common.append(x)
print("Common elements:", common)
