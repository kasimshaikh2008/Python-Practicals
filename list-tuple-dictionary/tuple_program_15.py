# Tuple Program 15
t = (45, 12, 78, 34, 90, 23, 67, 5, 89, 56)
big = t[0]
small = t[0]
for x in t:
    if x > big:
        big = x
    if x < small:
        small = x
print("Maximum:", big)
print("Minimum:", small)
