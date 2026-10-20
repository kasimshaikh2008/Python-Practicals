# Tuple Program 13
s = input("Enter a string: ")
new = ""
for ch in s:
    if ch == 'o':
        new = new + '@'
    else:
        new = new + ch
print(new)
