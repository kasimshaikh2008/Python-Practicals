# Program 38: Create a list of prime numbers up to 100.

primes = []
for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print("Prime numbers up to 100:")
print(primes)
