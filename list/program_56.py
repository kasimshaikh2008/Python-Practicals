# Program 56: Accept a list of integers and rotate the list by k positions (left and right).

numbers = []
data = input("Enter numbers separated by space: ").split()
for x in data:
    numbers.append(int(x))
k = int(input("Enter k: "))
k = k % len(numbers)

left = numbers[k:] + numbers[:k]
right = numbers[-k:] + numbers[:-k]

print("Original list:", numbers)
print("Left rotation by", k, ":", left)
print("Right rotation by", k, ":", right)
