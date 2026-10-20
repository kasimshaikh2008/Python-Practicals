# Program 20: Find elements present in one list but not another.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = []
for x in list1:
    if x not in list2:
        result.append(x)
print("In list1 but not in list2:", result)
