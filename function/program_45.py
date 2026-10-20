# Function Program 45

n = int(input("How many elements: "))
l = []
for i in range(n):
    l.append(input("Enter element: "))
result = list(map(lambda x: x.isdigit(), l))
print(result)
