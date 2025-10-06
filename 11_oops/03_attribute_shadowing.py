# ------------------------------------
# Attribute Shadowing in Python
# ------------------------------------

"""
? What is Attribute Shadowing
- Attribute shadowing happens when an **instance (object)** defines an attribute 
  with the same name as a **class attribute**.
- The object’s attribute will **override (shadow)** the class attribute
  for that specific object only.
- The class attribute still exists, but the object’s version takes priority.

👉 Key Point:
- Python first checks the **object’s namespace**.
- If not found → it looks into the **class namespace**.
"""

# ------------------------------------
# Example: Chai Class
# ------------------------------------

class Chai:
    temperature = "hot"    # Class attribute
    strength = "strong"    # Class attribute


# Creating object
cutting = Chai()

# Accessing class attribute via object
print(cutting.temperature)  # hot

# Shadowing: overriding class attribute in object namespace
cutting.temperature = "Mild"   # only for this object
cutting.cup = "Large"          # new attribute in object only

print("After changing:", cutting.temperature)  # Mild
print("Cup size:", cutting.cup)                # Large

# Class attribute is unaffected
print("Direct look into the class:", Chai.temperature)  # hot

# ------------------------------------
# Deleting Object Attributes
# ------------------------------------

# Remove the object attribute 'temperature'
del cutting.temperature

# Now Python falls back to the class attribute
print(cutting.temperature)  # hot

# Remove object-only attribute
del cutting.cup

# ❌ This will give AttributeError (cup only existed in object, not class)
# print(cutting.cup)

"""
Output:
hot
After changing: Mild
Cup size: Large
Direct look into the class: hot
hot
Traceback (most recent call last):
    ...
AttributeError: 'Chai' object has no attribute 'cup'
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- If an object defines an attribute with the same name as class → it SHADOWS the class attribute.
- Deleting the object’s attribute reveals the class attribute again.
- Object-specific attributes that don’t exist in class will raise error if deleted.
"""