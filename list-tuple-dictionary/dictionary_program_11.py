# Dictionary Program 11
marks = {}
n = int(input("How many students: "))
for i in range(n):
    rollno = int(input("Enter roll no: "))
    m = []
    for j in range(5):
        m.append(int(input("Enter marks of subject " + str(j + 1) + ": ")))
    marks[rollno] = m
print(marks)
