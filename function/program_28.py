# Function Program 28

stud = [{'name': 'Amit', 'age': 25}, {'name': 'Bina', 'age': 22}, {'name': 'Dax', 'age': 25}]
result = sorted(stud, key=lambda x: (x['age'], x['name']))
print(result)
