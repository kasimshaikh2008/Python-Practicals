# Program 46: Merge two lists, remove duplicates, sort the final list and display in ascending and descending order.

list1 = [5, 3, 8, 1, 3]
list2 = [8, 2, 9, 1, 7]

merged = list1 + list2
print("Merged list:", merged)

unique = []
for n in merged:
    if n not in unique:
        unique.append(n)
print("After removing duplicates:", unique)

unique.sort()
print("Ascending order:", unique)

unique.reverse()
print("Descending order:", unique)
