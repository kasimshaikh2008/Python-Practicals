# Function Program 12

fruits = ["Apple", "Mango", "Banana", "Orange"]
def add_fruit(fruit):
    global fruits
    fruits.append(fruit)
def insert_fruit(fruit, pos=1):
    globals()['fruits'].insert(pos, fruit)
def update_fruit(old, new):
    global fruits
    i = fruits.index(old)
    fruits[i] = new
def remove_fruit(x):
    global fruits
    if type(x) == int:
        fruits.pop(x)
    else:
        fruits.remove(x)
def arrange_fruits():
    global fruits
    fruits.sort()
add_fruit("Grapes")
print(fruits)
insert_fruit("Kiwi", 2)
print(fruits)
insert_fruit("Papaya")
print(fruits)
update_fruit(new="Pineapple", old="Mango")
print(fruits)
remove_fruit(0)
print(fruits)
remove_fruit("Orange")
print(fruits)
arrange_fruits()
print(fruits)
