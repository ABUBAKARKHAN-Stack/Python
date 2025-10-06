# ------------------------------------
# Static Methods in Python
# ------------------------------------

"""
? What are Static Methods
Static methods are **utility methods** that belong to a class but **don’t depend**
on any instance (`self`) or class (`cls`) variables.

They behave just like **normal functions**, but are logically grouped inside a class
because they are related to it conceptually.

You can call them **directly from the class** without creating an object.

---

🧩 Key Points:
- Defined using the `@staticmethod` decorator.
- Do **not** take `self` or `cls` as the first argument.
- Often used for **helper**, **utility**, or **data-processing** tasks.
- Can be called both from the **class** and an **instance** (but preferred via class).

---
"""

# ------------------------------------
# Example: Chai Utilities Class
# ------------------------------------

class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        """
        Cleans up a comma-separated string of ingredients.
        - Strips spaces.
        - Splits by commas.
        """
        return [item.strip() for item in text.split(",")]


# Sample input
raw = " water , milk , ginger   , honey"

# Calling static method directly from class (✅ Recommended way)
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)

# Optional: Can also be called from an object (⚠️ Not preferred)
# obj = ChaiUtils()
# cleaned = obj.clean_ingredients(raw)
# print(cleaned)

"""
Output:
['water', 'milk', 'ginger', 'honey']
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- Static methods don’t depend on class or instance data.
- Defined using @staticmethod decorator.
- Called directly using ClassName.method_name().
- Best for general-purpose helper logic related to the class.
"""