# Function Program 42

def extract_string(str_list1, l):
    return list(filter(lambda s: len(s) == l, str_list1))
str_list1 = ['Python', 'list', 'exercises', 'practice', 'solution']
l = 8
print(extract_string(str_list1, l))
