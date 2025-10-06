# ------------------------------------
# Accessing Base Class in Inheritance
# ------------------------------------

"""
? How to Access Base Class in Python
When a child class inherits from a base class, we often need to **initialize or reuse**
attributes/methods from the parent.  
There are **three ways** to do it:

1️⃣ **Code Duplication** → ❌ Not recommended  
   - You redefine parent attributes in child class manually.
   - Breaks DRY principle and hard to maintain.

2️⃣ **Explicit Base Class Call** → ⚙️ Acceptable  
   - You directly call the parent class’s `__init__()` using its name.
   - Useful when you need full control.

3️⃣ **super()** → ✅ Perfect & Recommended  
   - Automatically finds the parent class using Method Resolution Order (MRO).
   - Cleaner, scalable, and supports multiple inheritance.

---
"""

# ------------------------------------
# Base Class
# ------------------------------------
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# ------------------------------------
# ❌ 1. Code Duplication (Not Recommended)
# ------------------------------------
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level


# ------------------------------------
# ⚙️ 2. Explicit Base Class Call
# ------------------------------------
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level

# ginger = GingerChai("Ginger Classic Chai", 5, 3)


# ------------------------------------
# ✅ 3. Using super() (Best Practice)
# ------------------------------------
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)   # calls parent __init__()
        self.spice_level = spice_level


# Creating object of child class
ginger = GingerChai("Ginger Classic Chai", 5, 3)

print(f"Type: {ginger.type}")
print(f"Strength: {ginger.strength}")
print(f"Spice Level: {ginger.spice_level}")


# ------------------------------------
# 🧾 Expected Output
# ------------------------------------
"""
Type: Ginger Classic Chai
Strength: 5
Spice Level: 3
"""

# ------------------------------------
# ✅ Final Notes
# ------------------------------------
"""
- `super()` is the preferred way to access base class methods.
- It automatically handles method resolution order (MRO).
- Helps keep inheritance chains clean and scalable.
"""