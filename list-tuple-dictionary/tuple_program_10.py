# Tuple Program 10
# Pehle t4 tuple banate hain (Tuple Program 9 jaisa)
name = input("Enter your name: ")
hobbies = tuple(input("Enter hobbies (comma separated): ").split(","))
friends = tuple(input("Enter friends (comma separated): ").split(","))
degree = input("Enter your degree: ")
t4 = (name, hobbies, friends, degree)
print(t4)

item = input("Enter element to find: ")
found = False
for i in range(len(t4)):
    if type(t4[i]) == tuple:
        if item in t4[i]:
            print("Found at position", i, "and index", t4[i].index(item))
            found = True
    elif t4[i] == item:
        print("Found at position", i)
        found = True
if found == False:
    print("Not found")
