# Program 28: Find the index of the first/last occurrence of an element.

numbers = [5, 3, 7, 3, 9, 3]
x = 3
first = -1
last = -1
for i in range(len(numbers)):
    if numbers[i] == x:
        if first == -1:
            first = i
        last = i
print("First occurrence of", x, "at index", first)
print("Last occurrence of", x, "at index", last)
