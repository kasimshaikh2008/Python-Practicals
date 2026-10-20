# Program 54: Accept two lists of equal size and create a third list containing the sum of corresponding elements.

size = int(input("Enter size of lists: "))
list1 = []
list2 = []
print("Enter elements of first list:")
for i in range(size):
    list1.append(int(input()))
print("Enter elements of second list:")
for i in range(size):
    list2.append(int(input()))

list3 = []
for i in range(size):
    list3.append(list1[i] + list2[i])

print("List 1:", list1)
print("List 2:", list2)
print("Sum list:", list3)
