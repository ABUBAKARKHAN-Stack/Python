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