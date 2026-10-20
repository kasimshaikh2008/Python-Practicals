# Dictionary Program 7
emp = {101: "Raj", 102: "Amit", 103: "Neha", 104: "Priya"}
eid = int(input("Enter employee ID: "))
if eid in emp:
    emp[eid] = input("Enter new name: ")
    print(emp)
else:
    print("Employee not found")
