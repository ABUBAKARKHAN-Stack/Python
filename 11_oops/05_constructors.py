# ----------------------------
# Understanding __init__ Constructor
# ----------------------------

"""
? What is __init__
- `__init__` is a **special method** in Python classes (constructor).
- Called automatically when creating an object from a class.
- Used to initialize object attributes with given values.

👉 Key Points
- Always takes `self` as the first parameter.
- Lets you set instance-specific data at object creation.
- Runs automatically → no need to call it manually.
"""

# ----------------------------
# Example: Chai Orders
# ----------------------------
class ChaiOrder:
    def __init__(self, type_, size):
        # self.type & self.size become instance attributes
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"


# ----------------------------
# Creating Objects
# ----------------------------
order_one = ChaiOrder(type_="Masala", size=200)
print(order_one.summary())   # 200ml of Masala chai

order_two = ChaiOrder(type_="Ginger", size=220)
print(order_two.summary())   # 220ml of Ginger chai


# ----------------------------
# Expected Output
# ----------------------------
"""
200ml of Masala chai
220ml of Ginger chai
"""

# ----------------------------
# ✅ Final Notes
# ----------------------------
"""
- __init__ runs automatically when an object is created
- Used to initialize attributes of that object
- Each object can have its own values (different from class-level attributes)
"""