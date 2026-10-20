# Program 31: Find the intersection, union, and difference of two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
intersection = []
union = []
difference = []
for x in list1:
    if x in list2:
        intersection.append(x)
    else:
        difference.append(x)
    union.append(x)
for y in list2:
    if y not in union:
        union.append(y)
print("Intersection:", intersection)
print("Union:", union)
print("Difference (list1 - list2):", difference)
