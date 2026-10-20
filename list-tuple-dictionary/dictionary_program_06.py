# Dictionary Program 6
emp = {101: "Raj", 102: "Amit", 103: "Neha", 104: "Priya"}
eid = int(input("Enter employee ID: "))
if eid in emp:
    print("Name:", emp[eid])
else:
    name = input("Not available. Enter employee name: ")
    emp[eid] = name
    print(emp)
