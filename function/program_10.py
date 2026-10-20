# Function Program 10

def get_value(s):
    if s.isdigit():
        return int(s)
    try:
        return float(s)
    except:
        return s
a = get_value(input("Enter first value: "))
b = get_value(input("Enter second value: "))
print("Type of first value:", type(a))
print("Type of second value:", type(b))
try:
    print("Addition:", a + b)
except:
    print("Addition not possible")
try:
    print("Multiplication:", a * b)
except:
    print("Multiplication not possible")
