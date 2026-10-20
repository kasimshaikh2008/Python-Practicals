# Program 67: Menu-driven Student Record Management System using lists.

students = []
while True:
    print("\n1.Add  2.Display all  3.Search  4.Update  5.Delete")
    print("6.Sort by name  7.Sort by marks  8.Topper  9.Average marks  10.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        roll = int(input("Enter roll no: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students.append([roll, name, marks])
        print("Student added")
    elif ch == 2:
        if len(students) == 0:
            print("No records found")
        else:
            print("Roll No\tName\tMarks")
            for s in students:
                print(s[0], "\t", s[1], "\t", s[2])
    elif ch == 3:
        roll = int(input("Enter roll no to search: "))
        found = False
        for s in students:
            if s[0] == roll:
                print("Found:", s[0], s[1], s[2])
                found = True
        if not found:
            print("Student not found")
    elif ch == 4:
        roll = int(input("Enter roll no to update: "))
        found = False
        for s in students:
            if s[0] == roll:
                s[1] = input("Enter new name: ")
                s[2] = int(input("Enter new marks: "))
                print("Record updated")
                found = True
        if not found:
            print("Student not found")
    elif ch == 5:
        roll = int(input("Enter roll no to delete: "))
        found = False
        for s in students:
            if s[0] == roll:
                students.remove(s)
                print("Record deleted")
                found = True
                break
        if not found:
            print("Student not found")
    elif ch == 6:
        n = len(students)
        for i in range(n):
            for j in range(0, n - i - 1):
                if students[j][1] > students[j + 1][1]:
                    students[j], students[j + 1] = students[j + 1], students[j]
        print("Sorted by name")
    elif ch == 7:
        n = len(students)
        for i in range(n):
            for j in range(0, n - i - 1):
                if students[j][2] < students[j + 1][2]:
                    students[j], students[j + 1] = students[j + 1], students[j]
        print("Sorted by marks (highest first)")
    elif ch == 8:
        if len(students) == 0:
            print("No records found")
        else:
            topper = students[0]
            for s in students:
                if s[2] > topper[2]:
                    topper = s
            print("Topper:", topper[0], topper[1], topper[2])
    elif ch == 9:
        if len(students) == 0:
            print("No records found")
        else:
            total = 0
            for s in students:
                total += s[2]
            print("Average marks:", total / len(students))
    elif ch == 10:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
