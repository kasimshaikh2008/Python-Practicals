# Tuple Program 3
t2 = (78, 85, 90, 66, 72)
# without sum()
total = 0
for m in t2:
    total = total + m
print("Total marks:", total)
# with sum()
print("Total marks:", sum(t2))
