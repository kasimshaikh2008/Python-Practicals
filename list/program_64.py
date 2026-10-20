# Program 64: Create a frequency table of elements in a list.

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq = {}
for n in numbers:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print("Element\tFrequency")
for key in freq:
    print(key, "\t", freq[key])
