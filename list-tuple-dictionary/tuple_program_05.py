# Tuple Program 5
t1 = ("Rahul", "Kumar", "Sharma")
t2 = (78, 85, 90, 66, 72)
t3 = (t1, t2)
num = int(input("Enter a number: "))
found = False
for t in t3:
    if num in t:
        found = True
if found:
    print("Number is present")
else:
    print("Number is not present")
