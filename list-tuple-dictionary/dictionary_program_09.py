# Dictionary Program 9
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
