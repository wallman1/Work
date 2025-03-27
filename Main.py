from Inventory_management import *

# -------------------------------------------
# Unit Testing
# -------------------------------------------
def unit_test():
    """Test individual functions in isolation."""
    
    # Test adding products
    add_product('apple', 50)  # Adding 50 more apples
    add_product('banana', 20)  # Adding 20 more bananas

    
    # Test selling products
    result = sell_product('apple', 10)
    assert result is None, f"Expected None but got {result}"  # No error should occur
    assert check_availability('apple') == 40, "Apple stock should be 40 after selling 10."
    print(result)

    # Test insufficient stock. Trying to sell more than available - if you sell more than 20, this SHOULD NOT present an error.
    result = sell_product('banana', 200)  # Selling 200 should not raise an error - if it does, the sell_product function needs fixing.
    assert result == "Insufficient stock", f"Expected 'Insufficient stock' but got {result}."
    print(result)
    # TODO: Test selling a non-existent product (e.g., 'grape') and check behavior.
    result = sell_product("grape", 100)
    # For example, it should return "Insufficient stock" or similar.
    print(result)
# -------------------------------------------
# Integration Testing
# -------------------------------------------
def integration_test():
    """Test how different functions from the Inventory Management module work together."""
    
    # Add products to inventory
    add_product('apple', 50)
    add_product('banana', 30)

    # Sell some products
    sell_product('apple', 10)
    sell_product('banana', 5)

    # Check stock after selling
    apple_stock = check_availability('apple')
    banana_stock = check_availability('banana')
    grape_stock = check_availability("grape")
    # Print results for verification
    print("\n----- Integration Test Results -----")
    print(f"Apple stock after sale: {apple_stock} (Expected: 40)")  # 50 - 10
    print(f"Banana stock after sale: {banana_stock} (Expected: 25)")  # 30 - 5
    print(f"Grape srock after sale: {grape_stock}")

    # TODO: Test checking availability of a non-existent product (e.g., 'mango', should return 0).
    print(grape_stock)
    # TODO: Test total inventory value after sales
    print(f"Total inventory value: {total_inventory_value()} (Expected: 70)")

# -------------------------------------------
# System Testing
# -------------------------------------------
def system_test():
    """Test the system as a whole."""
    
    # Run through the entire process: adding, selling, checking availability
    add_product('apple', 50)
    add_product('banana', 30)
    sell_product('apple', 10)
    sell_product('banana', 5)

    sell_product("banana", -1)
    sell_product("banana", 1000)
    sell_product("grape", 100)
    # Check final availability and inventory value
    apple_stock = check_availability('apple')
    banana_stock = check_availability('banana')
    inventory_value = total_inventory_value()

    print("\n----- System Test Results -----")
    print(f"Apple stock: {apple_stock} (Expected: 40)")  # 50 - 10
    print(f"Banana stock: {banana_stock} (Expected: 25)")  # 30 - 5
    print(f"Total inventory value: {inventory_value} (Expected: 70)")  # (40 * 1.0) + (25 * 0.5)
    
    # TODO: Add tests for boundary conditions such as no stock or empty inventory.
    # For example, check if the inventory value is 0 when no products exist.

# -------------------------------------------
# Running the Tests
# -------------------------------------------
if __name__ == "__main__":
    # Run all tests - UNCOMMENT EACH FUNCTION ONE AT A TIME!
    print("Running Unit Test...")
    print(unit_test())

    print("\nRunning Integration Test...")
    integration_test()

    print("\nRunning System Test...")
    system_test()