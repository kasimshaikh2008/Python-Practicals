# Function Program 18

mixed = [10, "apple", 25, "ball", 7, "cat", 40]
get_int = lambda lst: [x for x in lst if type(x) == int]
print(get_int(mixed))
