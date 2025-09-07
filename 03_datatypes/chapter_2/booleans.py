# BOOLEANS

"""
? What are Booleans in Python?
Booleans are a datatype that represent one of two values: True or False.
They are also considered a subtype of integers, where True = 1 and False = 0. 
This is why we say "Booleans act like numbers" (called *upcasting*).
"""

is_boiling = True  # True behaves like 1
stir_count = 5
total_actions = is_boiling + stir_count  
# Here, True is converted to 1, so result = 1 + 5 = 6
print(f"Total actions: {total_actions}")  # Prints 6

"""
In Python, to check whether a value is truthy or falsy (boolean context), 
we use the built-in function ***bool()***.

It takes any object as an argument and returns either True or False 
depending on the rules of type conversion.

Examples:
- bool(1) → True
- bool(0) → False
- bool("Hello") → True (non-empty string)
- bool("") → False (empty string has length 0 → falsy)
- bool(None) → False (None means "nothing" → falsy)

Explanation:
1) In the first case, bool(1) → True because 1 is treated as True.
2) In the second case, bool(0) → False because 0 is treated as False.
3) In the third case, the string "Hello" has length > 0, so it's truthy → True.
4) In the fourth case, the empty string "" has length = 0, so it's falsy → False.
5) In the fifth case, None is treated as "no value," which is falsy → False.
"""

milk_present = None  # Assign None (no value)
print(f"Is There Milk?: {bool(milk_present)}")  
# Prints False → because None is falsy


# Boolean Logical Operators
"""
Python provides three logical operators for Booleans:
1) and → returns True if *both* conditions are True
2) or → returns True if *at least one* condition is True
3) not → inverts the boolean value (True → False, False → True)
"""

water_hot = True
tea_added = True
can_serve = water_hot and tea_added  
# 'and' checks if both conditions are True → True and True → True
print(f"Can serve chai? {can_serve}")  # Prints True

want_tea = True
need_cookies = False
serve = want_tea or need_cookies  
# 'or' checks if at least one condition is True → True or False → True
print(f"Want Tea Or Cookies? {serve}")  # Prints True

craving_for_tea = False
print(f"Craving for tea? {not craving_for_tea}")  
# 'not' inverts the value → not False = True


"""
👉 Official Docs for str methods:
https://docs.python.org/3/library/stdtypes.html#boolean-values
"""