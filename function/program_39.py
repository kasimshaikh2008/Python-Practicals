# Function Program 39

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
matrix = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter element: ")))
    matrix.append(row)
transpose = lambda m: [[row[i] for row in m] for i in range(len(m[0]))]
print("Matrix:", matrix)
print("Transpose:", transpose(matrix))
