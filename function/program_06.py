# Function Program 6

def check_range(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False
num = int(input("Enter a number: "))
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
if check_range(num, start, end):
    print("Number is in the range")
else:
    print("Number is not in the range")
