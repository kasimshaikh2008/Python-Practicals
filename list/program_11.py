# Program 11: Sort a list in ascending and descending order (without sort()).

numbers = [64, 25, 12, 22, 11]
asc = numbers.copy()
n = len(asc)
for i in range(n):
    for j in range(0, n - i - 1):
        if asc[j] > asc[j + 1]:
            temp = asc[j]
            asc[j] = asc[j + 1]
            asc[j + 1] = temp
desc = []
for i in range(len(asc) - 1, -1, -1):
    desc.append(asc[i])
print("Original:", numbers)
print("Ascending:", asc)
print("Descending:", desc)
