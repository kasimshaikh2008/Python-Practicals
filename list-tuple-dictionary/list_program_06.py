# List Program 6
L1 = ["Raj", "Amit", "Neha", "Priya", "Karan"]
L1.append("Sara")
name = input("Enter student name: ")
if name in L1:
    print("Total same name students:", L1.count(name))
    print("Position of first occurrence:", L1.index(name))
else:
    print("Student is not present")
