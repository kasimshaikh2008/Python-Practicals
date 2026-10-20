# Program 30: Interleave two lists.

list1 = [1, 3, 5]
list2 = [2, 4, 6]
result = []
for i in range(len(list1)):
    result.append(list1[i])
    result.append(list2[i])
print("Interleaved list:", result)
