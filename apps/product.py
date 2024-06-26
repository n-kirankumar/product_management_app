# product.py

class Product:
    """
    Represents a product with name, price, and quantity.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product available.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new instance of Product.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product available.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns:
            str: Formatted string representation of the product.
        """
        return f"{self.name}: ${self.price} ({self.quantity} available)"
