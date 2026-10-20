# Tuple Program 8
# Pehle cities tuple banate hain (Tuple Program 7 jaisa)
n = int(input("How many cities: "))
cities = ()
for i in range(n):
    c = input("Enter city name: ")
    cities = cities + (c,)
print(cities)

# with len()
for c in cities:
    print(c, len(c))
# without len()
for c in cities:
    count = 0
    for ch in c:
        count = count + 1
    print(c, count)
