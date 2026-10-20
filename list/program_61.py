# Program 61: Accept a list and check whether it is a palindrome without converting it into a string.

numbers = []
data = input("Enter numbers separated by space: ").split()
for x in data:
    numbers.append(int(x))

left = 0
right = len(numbers) - 1
is_palindrome = True
while left < right:
    if numbers[left] != numbers[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
