# List Program 8
L1 = ["Raj", "Amit", "Neha", "Priya", "Karan"]
L1.append("Sara")
name = input("Enter name to remove: ")
if name in L1:
    L1.remove(name)
    print(L1)
else:
    print("Student not found")
