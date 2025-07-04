# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.
def get_base_price(quantity, item_price):
    """
    Calculate the base price before any discounts.
    
    Args:
        quantity: Number of items
        item_price: Price per item
        
    Returns:
        float: Total base price (quantity * item_price)
    """
    return quantity * item_price

def get_discount_factor(base_price):
    """
    Determine the discount factor based on the base price.
    
    Args:
        base_price: Total price before discount
        
    Returns:
        float: Discount factor (0.95 for orders > 1000, 0.98 otherwise)
    """
    if base_price > 1000:
        return 0.95  # 5% discount for large orders
    else:
        return 0.98  # 2% discount for smaller orders

def get_price(quantity, item_price):
    """
    Calculate the final price including quantity discounts.
    
    Args:
        quantity: Number of items
        item_price: Price per item
        
    Returns:
        float: Final price after applying discount
    """
    # Calculate base price (quantity * item_price)
    base_price = get_base_price(quantity, item_price)
    # Get appropriate discount factor
    discount_factor = get_discount_factor(base_price)
    # Apply discount to get final price
    return base_price * discount_factor

def main():
    """
    Main function demonstrating price calculations with different scenarios.
    """
    # Test with different quantities and prices
    print(get_price(5, 100))    # Small order: 5 * 100 * 0.98 = 490
    print(get_price(5, 1000))   # Large order: 5 * 1000 * 0.95 = 4750
    print(get_price(5, 10000))  # Very large order: 5 * 10000 * 0.95 = 47500

main()