# ------------------------------------
# Namespaces in Python (Class vs Object)
# ------------------------------------

"""
? What is a Namespace
- A namespace is like a **container (dictionary)** that holds names (variables/attributes) mapped to objects (values).
- Every class and every object has its own namespace.

👉 Three important namespaces:
1. **Class Namespace** → shared across all objects (like a recipe shared by all chai cups ☕).
2. **Instance/Object Namespace** → specific to one object (like your personalized cup of chai 🍵).
3. **Built-in Namespace** → provided by Python (e.g., `print`, `len`, etc).

---

✅ Class Attributes vs Object Attributes:
- Class attributes belong to the class (all objects share them).
- Object attributes belong only to that specific object.

If an attribute is not found in an object’s namespace → Python looks into the class namespace.
"""

# ------------------------------------
# Example 1: Class Namespace
# ------------------------------------

class Chai:
    origin = "Pakistan"   # Class attribute (shared by all objects)

print(Chai.origin)   # Access directly → Pakistan

# Adding new class attribute dynamically
Chai.is_hot = True
print(Chai.is_hot)   # True

# ------------------------------------
# Example 2: Object Namespace
# ------------------------------------

# Creating an object
masala = Chai()

# Accessing class attributes from object
print(f"Masala Origin: {masala.origin}")  # Pakistan
print(f"Masala is_hot: {masala.is_hot}")  # True

# Overriding class attribute in object namespace
masala.is_hot = False   # only affects THIS object

print(f"Class Value: {Chai.is_hot}")      # True → still same in class
print(f"Masala Object Value: {masala.is_hot}")  # False → changed only for masala object

# Adding a completely new attribute to object
masala.ingredients = ["Masala", "Milk", "Ginger"]
print(masala.ingredients)

"""
Output:
Pakistan
True
Masala Origin: Pakistan
Masala is_hot: True
Class Value: True
Masala Object Value: False
['Masala', 'Milk', 'Ginger']
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- Class attributes live in the **class namespace** and are shared by all objects.
- Object attributes live in the **object’s namespace** (unique to each object).
- If Python doesn’t find an attribute in the object, it looks into the class namespace.
- You can even add new attributes dynamically to objects (not shared).
"""