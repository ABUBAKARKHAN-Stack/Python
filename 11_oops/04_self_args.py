# ------------------------------------
# Understanding self in Python Classes
# ------------------------------------

"""
? What is self
- `self` is a **reference to the current object (instance)** of the class.
- When you call a method on an object → Python automatically passes the object itself as the **first argument**.
- By convention, we name it `self`, but technically you can name it anything.

👉 Key Points:
- `self` allows you to access **instance attributes** and **methods** inside the class.
- When you call `obj.method()`, Python internally does: `Class.method(obj)`.
"""

# ------------------------------------
# Example: Chai Cup
# ------------------------------------

class ChaiCup:
    size = 150  # ml (class attribute)

    def describe(self):
        # self refers to the object calling this method
        return f"A {self.size}ml chai cup."


# Creating object
cup = ChaiCup()

# Calling method normally
print(cup.describe())  
# Behind the scenes → Python does this:
print(ChaiCup.describe(cup))  

# ------------------------------------
# Example 2: Shadowing with self
# ------------------------------------

cup_two = ChaiCup()
cup_two.size = 100   # object attribute shadows class attribute

print(cup_two.describe())         # A 100ml chai cup.
print(ChaiCup.describe(cup_two))  # Same result because self = cup_two

"""
Output:
A 150ml chai cup.
A 150ml chai cup.
A 100ml chai cup.
A 100ml chai cup.
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- `self` = current instance of the class.
- Python automatically passes it when calling methods on objects.
- `obj.method()` is the same as `Class.method(obj)`.
"""