# Tuple Program 14
vowels = ('a', 'e', 'i', 'o', 'u')
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch.lower() in vowels:
        count = count + 1
print("Total vowels:", count)
