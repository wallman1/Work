# Dictionary to store product quantities
inventory = {}

# Function to add products to the inventory
def add_product(product, quantity):
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity

add_product("apple",1)
print(inventory)

# Function to sell products (decrease product quantity)
def sell_product(product, quantity):
    if product in inventory and inventory[product] >= quantity:
        inventory[product] -= quantity
    else:
        return "Insufficient stock"

sell_product("apple",1)
print(inventory)
print(sell_product("apple",1))
add_product("apple",1)

# Function to check if a product is available
def check_availability(product):
    return inventory.get(product, 0)

print(check_availability("apple"))

# Function to get total inventory value (simple example assuming fixed price for each product)
def total_inventory_value():
    prices = {
        'apple': 1.0,
        'banana': 0.5,
        'cherry': 1.5
    }
    total_value = 0
    for product, quantity in inventory.items():
        total_value += quantity * prices.get(product, 0)
    return total_value

print(total_inventory_value())