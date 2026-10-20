# Dictionary Program 5
emp = {101: "Raj", 102: "Amit", 103: "Neha", 104: "Priya"}
eid = int(input("Enter employee ID: "))
if eid in emp:
    print("Employee is present")
else:
    print("Employee is not present")
