# List Program 9
L1 = ["Raj", "Amit", "Neha", "Priya", "Karan"]
L1.append("Sara")
name = input("Enter name to remove: ")
while name in L1:
    L1.remove(name)
print(L1)
