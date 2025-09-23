# ------------------------------------
# Set Comprehensions in Python
# ------------------------------------

"""
? What are Set Comprehensions
Set comprehensions are a **concise way** of creating sets in Python using just a single line of code.
They make code **cleaner**, **shorter**, and bring logic in one place instead of writing long loops.

General Syntax:
    {expression for item in iterable if condition}

👉 Note:
- You can use conditions (`if`) to filter elements.
- Variable names inside comprehension must be consistent with loop variables.
- You can also use multiple `for` loops.
- Final evaluated value will be placed inside the set.
- Sets automatically remove duplicates.

Why use Set Comprehensions?
- Cleaner code ✨
- Centralized logic in one line ⚡
- Removes duplicates automatically 🗑️
- Same result with fewer lines 🧹
"""

# ------------------------------------
# Example 1: Removing Duplicates
# ------------------------------------

favourite_chais = [
    "Masala Chai",
    "Ice Chai",
    "Ginger Chai",
    "Masala Chai",
    "Ginger Chai",
    "Masala Chai",
    "Lemon Chai",
    "Ginger Chai",
]

# Extract unique chai types
unique_chais = {chai for chai in favourite_chais}
print("Unique Chais:", unique_chais)

"""
Output:
Unique Chais: {'Ice Chai', 'Masala Chai', 'Ginger Chai', 'Lemon Chai'}
"""

# ------------------------------------
# Example 2: Extracting Unique Ingredients
# ------------------------------------

recipes = {
    "Masala Chai": ["ginger", "cardamom", "cloves"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "cloves"],
}

# Collect all unique spices used in recipes
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print("Unique Spices:", unique_spices)

"""
Output:
Unique Spices: {'ginger', 'milk', 'cardamom', 'cloves', 'black pepper'}
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- Set comprehensions are used to create sets in one line.
- Syntax: {expression for item in iterable if condition}.
- They help in **filtering** and **transforming** data quickly.
- Sets automatically remove duplicates.
- Much shorter and cleaner than traditional loops.

⚡ Next: We’ll explore **Dictionary Comprehensions**.
"""

