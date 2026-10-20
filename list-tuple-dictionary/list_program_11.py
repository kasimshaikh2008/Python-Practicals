# List Program 11
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'o', 'u']
count = 0
for ch in alpha:
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        count = count + 1
print("Total vowels:", count)
