# Tuple Program 11
t = (12, 7, 34, 21, 8, 15, 40, 9, 26, 33)
odd = ()
even = ()
for x in t:
    if x % 2 == 0:
        even = even + (x,)
    else:
        odd = odd + (x,)
print("Odd tuple:", odd)
print("Even tuple:", even)
