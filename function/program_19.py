# Function Program 19

mixed = [10, "apple", 25, "ball", 7, "cat", 40]
get_str = lambda lst: [x for x in lst if type(x) == str]
print(get_str(mixed))
# i) using filter()
print(list(filter(lambda x: type(x) == str, mixed)))
# ii) filter all vowels from the given string
s = input("Enter a string: ")
vowels = list(filter(lambda ch: ch.lower() in "aeiou", s))
print(vowels)
