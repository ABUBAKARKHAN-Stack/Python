"""
Datatypes Chapter 1: Objects & Mutability in Python

In Python, **everything is an object**.  
That means data types like strings, numbers, and booleans are actually class objects.  

Each object in Python has:
1. **Identity** → its unique memory location (`id()` function shows this).
2. **Type** → what kind of object it is (`int`, `str`, `list`, etc.).
3. **Value** → the actual data stored.

* Important: Objects in Python can be **mutable** (can change) or **immutable** (cannot change).  
To check mutability, we don’t compare values—we check if the **identity (`id`) stays the same** after modification.
"""

# ------------------------------
#  Example 1: Immutable Objects (int)
# ------------------------------

# Assigning sugar_amount to 2
sugar_amount = 2
print(f"Initial Sugar Amount: {sugar_amount}")

# Reassign sugar_amount to 10
sugar_amount = 10
print(f"Updated Sugar Amount: {sugar_amount}")

# Check immutability via `id`
print(f"ID of 2: {id(2)}")
print(f"ID of 10: {id(10)}")
print(f"ID of 2 again: {id(2)}")  # Always same as before

"""
?? Why does this happen?
- Integers are immutable in Python.
- When we assign `sugar_amount = 2`, Python stores `2` in memory.
- After `sugar_amount = 10`, Python does **not** modify the original object.
  Instead, it creates a new object (`10`) at a new memory location.
- The old object (`2`) is still stored somewhere in memory.
- This behavior is often referred to as **"pass by value/reference copy"**.
"""

# ------------------------------
#  Example 2: Mutable Objects (set)
# ------------------------------

# Creating an empty set
super_hero = set()
print(f"Super Heroes Set: {super_hero}")  
print(f"Set ID (before adding): {id(super_hero)}")

# Add values into the set
super_hero.add("Spiderman")
super_hero.add("Batman")
super_hero.add("Ironman")

# Check again after modification
print(f"Super Heroes Set (after adding): {super_hero}")
print(f"Set ID (after adding): {id(super_hero)}")

"""
?? Why is the ID same here?

- Sets are **mutable**.
- When we modify a set (add/remove items), Python does not create a new object.
- Instead, it updates the existing object in the same memory location.
- That’s why the `id` of the set remains the same before and after modification.

* Rule of Thumb:
- Immutable: Numbers, Strings, Tuples, Booleans.
- Mutable: Lists, Sets, Dictionaries.
"""

print("\nThat's all about Objects & Mutability in Python.")
