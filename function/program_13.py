# Function Program 13

def generate_prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
        if flag:
            primes.append(num)
        num = num + 1
    return primes
n = int(input("How many prime numbers: "))
print(generate_prime(n))
