# Function Program 14

mobiles = {}
def create():
    global mobiles
    mobiles = {"Samsung S21": [45000, "8GB RAM, 128GB storage"],
               "iPhone 12": [60000, "4GB RAM, 64GB storage"]}
def add_element(name, price, features):
    mobiles[name] = [price, features]
def update_element(name, price, features):
    if name in mobiles:
        mobiles[name] = [price, features]
    else:
        print("Mobile not found")
def delete_element(name):
    if name in mobiles:
        del mobiles[name]
    else:
        print("Mobile not found")
create()
print(mobiles)
add_element("Redmi Note 10", 15000, "6GB RAM, 128GB storage")
print(mobiles)
update_element("iPhone 12", 55000, "4GB RAM, 128GB storage")
print(mobiles)
delete_element("Samsung S21")
print(mobiles)
