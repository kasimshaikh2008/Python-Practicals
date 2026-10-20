# Program 25: Find the frequency of each element (build a dictionary).

numbers = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for n in numbers:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1
print("Frequency:", freq)
