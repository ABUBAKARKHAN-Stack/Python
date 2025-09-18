# ------------------------------------
# Functions: Built-in Functions in Python
# ------------------------------------

"""
? What are Built-in Functions

Python comes with many functions that are already defined for you.
They are called *built-in functions*. 
You don't need to import anything, they are available directly.

Examples: print(), len(), abs(), type(), help(), filter(), max(), etc.
"""

# Example 1: __doc__ and __name__ attributes
def chai_flavor(name="Masala"):
    """Return a chai flavor"""
    return name

print(chai_flavor.__doc__)   # Prints the docstring of the function
print(chai_flavor.__name__)  # Prints the function name
print(chai_flavor())         # Default argument will be "Masala"


# Example 2: help() function
help(len)   # Shows documentation about len()


# Example 3: abs() function
print(abs(-33))   # Gives absolute value => 33


# Example 4: filter() function with lambda
numbers = [1, 2, 3, 4, 5]
odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))
print(odd_numbers)   # [1, 3, 5]


# Example 5: type() function
print(type("Abubakar"))  # <class 'str'>


# Example 6: User-defined function with docstring
def generate_bill(chai, samosas):
    """
    Calculate The Total Bill for Chai and Samosa:
    * param chai: number of chai cups (10 rupees each)
    * param samosas: number of samosas (15 rupees each)
    * return: total amount with thank you message
    """
    total_amount = (chai * 10) + (samosas * 15)
    return f"Thank you! Total Bill: {total_amount}"


print(generate_bill(4, 3))   # 4 chai, 3 samosas

# ------------------------------------
# Docs Reference:
# https://docs.python.org/3/library/functions.html
# ------------------------------------