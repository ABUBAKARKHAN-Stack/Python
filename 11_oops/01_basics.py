# ------------------------------------
# Classes & Objects in Python (Basics)
# ------------------------------------

"""
? What are Classes in Python
- A class is a **blueprint** for creating objects.
- Objects are **instances** of a class.

👉 Analogy:
Think of a `Chai` class as the **recipe** for making chai ☕.
The actual cup of chai you drink is the **object (instance)** created from that recipe.

---

✅ Defining a Class:
class ClassName:
    pass   # placeholder (empty body)

✅ Creating an Object:
obj = ClassName()   # instance of the class

✅ type()
- `type(obj)` tells us the class of an object.
"""

# ------------------------------------
# Example 1: Defining Empty Classes
# ------------------------------------

class Chai:
    pass

class Chai_Time:
    pass

print(type(Chai))   # <class 'type'> → Because Chai itself is a class

# ------------------------------------
# Example 2: Creating an Object (Instance)
# ------------------------------------

ginger_tea = Chai()   # Making a "chai cup" ☕

print(type(ginger_tea))             # <class '__main__.Chai'>
print(type(ginger_tea) is Chai)     # True → belongs to Chai
print(type(ginger_tea) is Chai_Time) # False → not from Chai_Time class

"""
Output:
<class 'type'>
<class '__main__.Chai'>
True
False
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- A class is a blueprint (like recipe).
- An object is an instance (like an actual cup of chai).
- `type(obj)` shows the class it belongs to.
- Different classes create different types of objects.
"""