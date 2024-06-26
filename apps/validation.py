# validation.py

def validate_price(price):
    """
    Validates the price input.

    Args:
        price (str): The price input to validate.

    Returns:
        float: Validated price as a float.

    Raises:
        ValueError: If price is not a positive number or cannot be converted to float.
    """
    try:
        price = float(price)
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        return price
    except ValueError:
        raise ValueError("Invalid price format.")

def validate_quantity(quantity):
    """
    Validates the quantity input.

    Args:
        quantity (str): The quantity input to validate.

    Returns:
        int: Validated quantity as an integer.

    Raises:
        ValueError: If quantity is not a positive integer or cannot be converted to int.
    """
    try:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        return quantity
    except ValueError:
        raise ValueError("Invalid quantity format.")

def validate_name(name):
    """
    Validates the product name input.

    Args:
        name (str): The product name input to validate.

    Returns:
        str: Validated product name as a stripped string.

    Raises:
        ValueError: If product name is empty or consists only of whitespace.
    """
    if not name.strip():
        raise ValueError("Product name cannot be empty.")
    return name.strip()

