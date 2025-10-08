# ------------------------------------
# Handling Multiple Exceptions in Python
# ------------------------------------

"""
? Why handle multiple exceptions
In Python, different kinds of errors can occur in the same block of code.
We can catch and handle multiple types of exceptions separately for 
more accurate and meaningful error messages.

✅ Example:
- KeyError → When a key is not found in a dictionary.
- TypeError → When an operation or function is applied to the wrong type.
"""

# ------------------------------------
# Example: Handling Multiple Errors
# ------------------------------------

def process_order(item, quantity):
    try:
        # Lookup price
        price = {"masala": 20}[item]
        
        # Check if quantity is a valid number
        if not isinstance(quantity, (int, float)):
            raise TypeError
        
        # If all is good, calculate total
        print(f"Total Price: {price * quantity}")

    # Handle specific exceptions one by one
    except KeyError:
        print("Sorry, that chai is not on the menu.")
    except TypeError:
        print("Quantity must be a number.")


# Test cases
process_order("ginger", 4)
process_order("masala", "two")
process_order("masala", 10)


# ------------------------------------
# 🧾 Output:
# ------------------------------------
"""
Sorry, that chai is not on the menu.
Quantity must be a number.
Total Price: 200
"""

# ------------------------------------
# ✅ Final Summary:
# ------------------------------------
"""
- You can handle **different exception types** using multiple `except` blocks.
- This allows you to respond appropriately to each kind of error.
- Always handle specific exceptions before general ones (for clarity).
"""