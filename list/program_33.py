# Program 33: Group elements by a condition (odd/even, length of strings).

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
groups = {"even": [], "odd": []}
for n in numbers:
    if n % 2 == 0:
        groups["even"].append(n)
    else:
        groups["odd"].append(n)
print("Grouped by odd/even:", groups)

words = ["cat", "dog", "apple", "mango", "elephant", "rat"]
by_length = {}
for w in words:
    l = len(w)
    if l not in by_length:
        by_length[l] = []
    by_length[l].append(w)
print("Grouped by length:", by_length)
