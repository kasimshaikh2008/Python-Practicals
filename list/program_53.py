# Program 53: Create a list of 20 numbers and remove all prime numbers from the list.

numbers = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
result = []
for num in numbers:
    is_prime = True
    if num < 2:
        is_prime = False
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if not is_prime:
        result.append(num)
print("Original list:", numbers)
print("After removing primes:", result)
