# Tuple Program 9
name = input("Enter your name: ")
hobbies = tuple(input("Enter hobbies (comma separated): ").split(","))
friends = tuple(input("Enter friends (comma separated): ").split(","))
degree = input("Enter your degree: ")
t4 = (name, hobbies, friends, degree)
print(t4)
