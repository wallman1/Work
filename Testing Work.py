# inventory_management.py

# Dictionary to store product quantities
inventory = {
    'apple': 50,
    'banana': 30,
    'cherry': 20
}

# Function to add products to the inventory
def add_product(product, quantity):
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity

add_product("apple", 10)

# Function to sell products (decrease product quantity)
def sell_product(product, quantity):
    if product in inventory and inventory[product] >= quantity:
        inventory[product] -= quantity
    else:
        return "Insufficient stock"

sell_product("banana", 30)

# Function to check if a product is available
def check_availability(product):
    return inventory.get(product, 0)

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

total_inventory_value()
