# ------------------------------------
# Sets
# ------------------------------------

"""
? What are Sets in Python?
Sets are a built-in mutable data type in Python that allow you to store multiple items in a single variable.
They are:
    - Unordered (elements do not maintain insertion order in older Python versions).
    - Contain only unique elements (no duplicates).
  General Syntax:
    <variable_name> = {value1, value2, value3, ...}
"""

# Definition
essential_spices = {"cardamom", "ginger", "cinnamon"}
print(f"Essential Spices: {essential_spices}")

# ------------------------------------
# Set Mutation Methods
# ------------------------------------

# add()
"""
add() method is used to add an element into a set.
If the element already exists, it will not be added again since sets store only unique values.
"""
essential_spices.add("lemon")
print(f"Essential Spices after adding 'lemon': {essential_spices}")

# remove()
"""
remove() method removes a specified element from the set.
⚠️ Note: If the element is not found, it will raise a KeyError.
Also, removal is case-sensitive and must match the exact element.
"""
essential_spices.remove("lemon")
print(f"Essential Spices after removing 'lemon': {essential_spices}")

# ------------------------------------
# Union of Sets
# ------------------------------------

# union()
"""
union() method combines all elements from two or more sets (removing duplicates).
"""
optional_spices = {"cloves", "ginger", "black pepper"}
all_spices = essential_spices.union(optional_spices)
print(f"All Spices (using union()): {all_spices}")

# Alternative way: Using | operator
all_spices2 = essential_spices | optional_spices
print(f"All Spices (using | operator): {all_spices2}")

# ------------------------------------
# Intersection of Sets (Common Elements)
# ------------------------------------

# intersection()
"""
intersection() method returns only the common elements between sets.
"""
common_spices = essential_spices.intersection(optional_spices)
print(f"Common Spices (using intersection()): {common_spices}")

# Alternative way: Using & operator
common_spices2 = essential_spices & optional_spices
print(f"Common Spices (using & operator): {common_spices2}")

# ------------------------------------
# Difference between Sets
# ------------------------------------

# difference()
"""
difference() method returns elements that are in the first set but not in the second.
"""
only_in_essential = essential_spices.difference(optional_spices)
print(f"Only in Essential Spices (using difference()): {only_in_essential}")

# Alternative way: Using - operator
only_in_essential2 = essential_spices - optional_spices
print(f"Only in Essential Spices (using - operator): {only_in_essential2}")

# ------------------------------------
# Membership Testing
# ------------------------------------
"""
We can test if an element is present in a set using the 'in' keyword.
It returns True if found, False otherwise.
"""
print(f"Is 'ginger' present in essential spices? {'ginger' in essential_spices}")

# ------------------------------------
# Note:
# ------------------------------------
"""
There are many other useful set methods in Python 
(like discard(), clear(), isdisjoint(), issubset(), issuperset(), etc.).
We will explore them later.

? Related Data Type:
Python also provides frozenset(), which is very similar to set but is immutable.
That means once created, you cannot modify (add/remove) its elements.

📌 Official Documentation:
https://docs.python.org/3/library/stdtypes.html#set
"""
