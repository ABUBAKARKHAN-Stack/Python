# Tuples

"""
? What are Tuples in Python?
Tuples are collections that can store different types of data such as strings, integers, booleans, etc.
They are also immutable (once created, their values cannot be changed).
General Syntax:
    <variable_name> = (value1, value2, value3, ...)
    
Tuples are very powerful and widely used in Python.
"""

masala_spices = ("cardamom", "cloves", "cinnamon")

# Destructuring values from a tuple
(spice1, spice2, spice3) = masala_spices
print(f"Main Masala Spices: {spice1}, {spice2}, {spice3}")

# Another way of creating tuples
ginger_ratio, cardamom_ratio = 2, 1
"""
Behind the scenes, Python interprets this as:
    (ginger_ratio, cardamom_ratio) = (2, 1)
This is the Pythonic way of working with tuples.
"""
print(f"Ginger Ratio: {ginger_ratio}")
print(f"Cardamom Ratio: {cardamom_ratio}")

"""
An interesting feature:
We can easily swap values using tuple unpacking.
This is a short and elegant way to swap variables without a temporary variable.
"""
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Switched Ginger Ratio: {ginger_ratio}")
print(f"Switched Cardamom Ratio: {cardamom_ratio}")

# Membership check
teas = ("Masala", "Lemon", "Ginger")
print(f"Is Masala present? {'Masala' in teas}")
"""
Note:
Membership checks are case-sensitive.
For example, 'Ginger' is valid, but 'ginger' will return False.
"""

# Length of a tuple
print(f"Number of Teas: {len(teas)}")

"""
Note:
- Tuples are immutable → once created, values cannot be changed.
  Example: masala_spices[0] = "pepper" will raise an error.
- Tuples are often used when you want a fixed collection of items.
- Common tuple methods include:
    - count(value): Returns how many times a value appears in the tuple.
    - index(value): Returns the index of the first occurrence of the value.

Example:
    numbers = (1, 2, 3, 2, 4)
    print(numbers.count(2))   # Output: 2
    print(numbers.index(3))   # Output: 2

📘 Official Docs: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
"""
