# Program 48: Create a list of employee names. Search for a name, update it if found, otherwise add it to the list.

employees = ["Amit", "Neha", "Rahul", "Priya"]
print("Employee list:", employees)

name = input("Enter name to search: ")
if name in employees:
    new_name = input("Name found. Enter new name: ")
    index = employees.index(name)
    employees[index] = new_name
    print("Name updated")
else:
    employees.append(name)
    print("Name not found, so it was added")

print("Updated list:", employees)
