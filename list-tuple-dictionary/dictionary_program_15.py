# Dictionary Program 15
fruits = {}
for i in range(6):
    name = input("Enter fruit name: ")
    buy = float(input("Enter buying price: "))
    sell = float(input("Enter selling price: "))
    fruits[name] = (buy, sell)
print("Fruits with profit:")
for f in fruits:
    if fruits[f][0] < fruits[f][1]:
        print(f)
print("Fruits with loss:")
for f in fruits:
    if fruits[f][0] > fruits[f][1]:
        print(f)
print("Fruits with no profit no loss:")
for f in fruits:
    if fruits[f][0] == fruits[f][1]:
        print(f)
