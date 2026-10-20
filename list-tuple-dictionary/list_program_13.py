# List Program 13
employees = [["Raj", 25, 30000, "Python"],
             ["Amit", 30, 45000, "Java"],
             ["Neha", 28, 40000, "Web Design"]]
name = input("Enter employee name: ")
found = False
for emp in employees:
    if emp[0] == name:
        print("Name:", emp[0])
        print("Age:", emp[1])
        print("Salary:", emp[2])
        print("Expertise:", emp[3])
        found = True
if found == False:
    print("Error: Employee not found")
