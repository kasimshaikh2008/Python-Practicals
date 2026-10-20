# Dictionary Program 14
data = {}
for i in range(5):
    rollno = input("Enter roll no: ")
    m = input("Enter 6 marks (comma separated): ").split(",")
    data[rollno] = [int(x) for x in m]
minimum = {}
maximum = {}
for sub in range(6):
    col = []
    for r in data:
        col.append(data[r][sub])
    minimum["Subject " + str(sub + 1)] = min(col)
    maximum["Subject " + str(sub + 1)] = max(col)
print("Minimum marks:", minimum)
print("Maximum marks:", maximum)
