# Program 62: Create a matrix using nested lists and perform addition, transpose, sum of each row and sum of each column.

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
rows = len(A)
cols = len(A[0])

print("Matrix A:")
for row in A:
    print(row)
print("Matrix B:")
for row in B:
    print(row)

add = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    add.append(row)
print("\nMatrix addition:")
for row in add:
    print(row)

transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(A[i][j])
    transpose.append(row)
print("\nTranspose of A:")
for row in transpose:
    print(row)

print("\nSum of each row of A:")
for i in range(rows):
    print("Row", i + 1, ":", sum(A[i]))

print("\nSum of each column of A:")
for j in range(cols):
    total = 0
    for i in range(rows):
        total += A[i][j]
    print("Column", j + 1, ":", total)
