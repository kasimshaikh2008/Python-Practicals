# Tuple Program 12
t = tuple(input("Enter elements separated by space: ").split())
for i in range(len(t) - 1, -1, -1):
    print(t[i])
