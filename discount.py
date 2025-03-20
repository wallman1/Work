def calculate_total(price, quantity):
    total = price * quantity  # Line 3
    return total  # Line 4

def apply_discount(total, discount):
    return total - (total * discount)  # Line 6

def main():
    price = 100
    quantity = 5
    discount = 10  #
    total = calculate_total(price, quantity)  # Line 10
    total_after_discount = apply_discount(total)  # Line 11
    print(f"Total after discount: {total_after_discount}")  # Line 12

main()