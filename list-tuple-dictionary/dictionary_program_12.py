# Dictionary Program 12
# Pehle marks dictionary banate hain (Dictionary Program 11 jaisa)
marks = {}
n = int(input("How many students: "))
for i in range(n):
    rollno = int(input("Enter roll no: "))
    m = []
    for j in range(5):
        m.append(int(input("Enter marks of subject " + str(j + 1) + ": ")))
    marks[rollno] = m
print(marks)

result = {}
for r in marks:
    total = sum(marks[r])
    per = total / 5
    if per >= 75:
        grade = "A"
    elif per >= 60:
        grade = "B"
    elif per >= 40:
        grade = "C"
    else:
        grade = "Fail"
    result[r] = (total, per, grade)
print(result)
