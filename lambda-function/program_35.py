# Program 35: Increase selected salaries by 10%

salaries = [30000, 45000, 50000, 65000]
selected = filter(lambda salary: salary > 40000, salaries)
new_salaries = list(map(lambda salary: round(salary * 1.10, 2), selected))
print(new_salaries)
