"""
Datatypes Chapter 2: Immutable Datatypes
There are 5 Basic Immutable Datatypes in Python: Numbers, Boolean, String, Tuples, Frozensets, Bytes
"""

# NUMBERS
"""
? What are numbers in Python?
Numbers are objects (instances of classes) that are used to perform mathematical operations such as 
addition, multiplication, subtraction, division, etc.

* There are different types of numbers in Python:
*** Integers, Floats, Booleans, Complex ***
"""

# Integers
ginger_tea_grams = 5  # Assign 5 (datatype: int) to ginger_tea_grams variable
black_tea_grams = 10  # Assign 10 (datatype: int) to black_tea_grams variable
total_tea_grams = ginger_tea_grams + black_tea_grams  # Basic addition operation
print(f"Total Tea in grams is: {total_tea_grams}")  # Prints 15

remaining_tea_grams = black_tea_grams - ginger_tea_grams  # Subtraction operation
print(f"Remaining Tea in grams is: {remaining_tea_grams}")  # Prints 5

milk_liters = 9  # Assign 9 (datatype: int) to milk_liters variable
servings = 5  # Assign 5 (datatype: int) to servings variable
milk_per_servings = milk_liters / servings  
# Basic division operation. Division always produces a float result, 
# even if both operands are integers. This shows how Python can implicitly
# convert integers into floats.
print(f"Milk Per Serving is: {milk_per_servings}")  # Prints 1.8

total_tea_bags = 9
pots = 5
bags_per_pot = total_tea_bags // pots  
# Floor division: Divides total_tea_bags by pots but discards any fractional part, 
# always returning an integer result.
print(f"Bags per pot is: {bags_per_pot}")  # Prints 1

total_cardmom_pods = 10
pods_per_cup = 3
left_over_pods = total_cardmom_pods % pods_per_cup  
# Modulus operator: Returns the remainder of the division.
print(f"Left Over Pods are: {left_over_pods}")  # Prints 1

num_1 = 10
power_of_num_1 = 3
result = num_1 ** power_of_num_1  
# Exponentiation operator: raises num_1 to the power of power_of_num_1
# Equivalent to 10 * 10 * 10 = 1000
print(f"10 Power 3 is: {result}")  # Prints 1000

total_tea_leaves_harvested = 1_000_000_000  
# Using underscores improves readability for large numbers
print(f"Total Tea Leaves Harvested: {total_tea_leaves_harvested}")  # Prints 1000000000


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


# STRINGS
"""
? What are Strings in Python?
Strings are a collection of characters. 
They are used to store and manipulate text data like words, sentences, or symbols.
We can manipulate them based on our requirements.
"""

# Definition
chai_type = "Masala Tea"
customer_name = "Abubakar"
print(f"Order for {customer_name} :: {chai_type} please!")  
# Prints: Order for Abubakar :: Masala Tea please!


# Strings Indexing and Slicing
"""
In Python, the index of a string starts from 0 and goes up to its length - 1.

For example: "Hello" → length is 5
Indexes:
0 → H
1 → e
2 → l
3 → l
4 → o

To extract parts of a string we use indexing and slicing.
Syntax: string[startIndex:endIndex]
Note: The endIndex is exclusive (not included).

Example:
greet = "Hello"
print(greet[0:4])  # Prints "Hell"
"""

chai_description = "Aromatic and Bold"

# Slice first word → indexes 0 to 7 (end exclusive → 8)
print(f"First word: {chai_description[0:8]}")  
# Same as chai_description[:8] → Prints "Aromatic"

# Slice last word → starting from index 12 to end
print(f"Last word: {chai_description[12:]}")  
# Prints "Bold"

# Step slicing → pick every 3rd character from index 0 to 15
print(f"Every third char: {chai_description[0:16:3]}")  
# Prints "Amia l"

# Reversing a string using slicing
# [: : -1] means start from end (-1) and move backwards
print(f"Reverse: {chai_description[::-1]}")  
# Prints "dloB dna citamorA"


# String Length
"""
In Python, we can find the total number of characters in a string (including spaces)
using the built-in len() function.
"""

chai_length = len(chai_description)
print(f"Length of chai_description is: {chai_length}")  
# Prints 16 → because "Aromatic and Bold" has 16 characters (including spaces)


# String Case Methods
masala_tea = "masala tea"

# To uppercase
uppercase_masala_tea = masala_tea.upper()
print(uppercase_masala_tea)  # MASALA TEA

# To lowercase
lowercase_masala_tea = masala_tea.lower()
print(lowercase_masala_tea)  # masala tea


# Encoding and Decoding
"""
Encoding: Converting string → bytes
Decoding: Converting bytes → string

UTF-8 is the most common encoding used in Python.
"""

label_text = "Chai Speciあl"
encoded_text = label_text.encode("utf-8")  # Encode to bytes
decoded_text = encoded_text.decode("utf-8")  # Decode back to string

print(f"Label Text with special char: {label_text}")
print(f"Encoded Label Text: {encoded_text}")
print(f"Decoded Label Text: {decoded_text}")


# Finding characters in strings
hot_tea = "Lemon Tea"

# Find index of first 'e'
print(hot_tea.find("e"))  # Prints 1

# Find index of 'e' starting search from index 4
print(hot_tea.find("e", 4))  # Prints 7


"""
Note:
There are many other string methods in Python (like replace, split, strip, join, etc.)

👉 Official Docs for str methods:
https://docs.python.org/3/library/stdtypes.html#string-methods
"""