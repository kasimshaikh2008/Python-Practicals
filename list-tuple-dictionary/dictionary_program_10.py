# Dictionary Program 10
# Pehle students dictionary banate hain (Dictionary Program 9 jaisa)
students = {}
for i in range(5):
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    degree = input("Enter degree: ")
    subject = input("Enter favorite subject: ")
    initial = ""
    for w in name.split():
        initial = initial + w[0].upper()
    students[initial] = [age, degree, subject]
print(students)

young = None
for k in students:
    if young == None or students[k][0] < students[young][0]:
        young = k
print("Youngest student:", young, students[young])
