# Function Program 7

def count_case(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1
    return upper, lower
s = input("Enter a string: ")
u, l = count_case(s)
print("Uppercase characters:", u)
print("Lowercase characters:", l)
