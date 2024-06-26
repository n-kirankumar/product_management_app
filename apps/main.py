# main.py

from product import Product
from validation import validate_name, validate_price, validate_quantity
from makelog import log_info, log_error  # Import logging functions from makelog.py


def add_product(products):
    """
    Adds a new product to the product list.

    Args:
        products (list): The list of products to add the new product to.

    Returns:
        str: Message indicating success or failure of the operation.
    """
    log_info("add_product function started.")
    try:
        name = input("Enter product name: ")
        name = validate_name(name)
        price = input("Enter product price: ")
        price = validate_price(price)
        quantity = input("Enter product quantity: ")
        quantity = validate_quantity(quantity)

        product = Product(name, price, quantity)
        products.append(product)
        log_info(f"Added product: {name}")
        return "Product added successfully."
    except ValueError as e:
        log_error(f"Error adding product: {e}")
        return f"Error: {e}"
    finally:
        log_info("add_product function ended.")


def list_products(products):
    """
    Lists all products in the product list.

    Args:
        products (list): The list of products to display.

    Returns:
        str: String representation of all products.
    """
    log_info("list_products function started.")
    if not products:
        log_info("No products found.")
        return "No products found."
    else:
        product_list = "\n".join([f"{idx + 1}. {str(product)}" for idx, product in enumerate(products)])
        log_info("Products listed.")
        return product_list
    log_info("list_products function ended.")


def main():
    """
    Main function to run the Product Management Application.

    Returns:
        str: Message indicating completion of the application.
    """
    log_info("main function started.")
    products = []
    while True:
        print("\nProduct Management Menu:")
        print("1. Add a product")
        print("2. List all products")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            result = add_product(products)
            log_info(result)
        elif choice == '2':
            result = list_products(products)
            log_info(result)
            print(result)  # Print products list to console
        elif choice == '3':
            break
        else:
            log_error("Invalid choice entered.")
            print("Invalid choice. Please enter a valid option.")

    log_info("main function ended.")
    return "Application finished successfully."


if __name__ == "__main__":
    log_info("Application started.")
    result = main()
    log_info(result)
    log_info("Application ended.")
