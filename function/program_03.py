# Function Program 3

def to_binary(n):
    return bin(n)
def to_octal(n):
    return oct(n)
def to_hexa(n):
    return hex(n)
num = int(input("Enter a decimal number: "))
print("Binary:", to_binary(num))
print("Octal:", to_octal(num))
print("Hexadecimal:", to_hexa(num))
