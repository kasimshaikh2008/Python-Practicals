# Dictionary Program 8
emp = {101: "Raj", 102: "Amit", 103: "Neha", 104: "Priya"}
eid = int(input("Enter employee ID to remove: "))
if eid in emp:
    emp.pop(eid)
    print(emp)
else:
    print("Employee not found")
