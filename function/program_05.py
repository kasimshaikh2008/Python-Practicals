# Function Program 5

def multiply(lst):
    result = 1
    for x in lst:
        result = result * x
    return result
nums = [2, 3, 4, 5]
print("Multiplication:", multiply(nums))
