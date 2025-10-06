# ------------------------------------
# Class Methods in Python
# ------------------------------------

"""
? What are Class Methods
Class methods are **methods that work with the class itself** rather than its instances.
They are defined using the **@classmethod** decorator and take `cls` (not `self`) as the first argument.

They’re most commonly used for:
- Creating **alternative constructors**.
- Performing operations that affect the **entire class**, not just a single object.

---

🧩 Key Points:
- Declared with `@classmethod` decorator.
- First parameter is always `cls` → refers to the class, not the object.
- Can be called directly using the **class name**.
- Often used to **instantiate objects** in different ways (e.g., from dicts, strings, JSON, etc.).

---
"""

# ------------------------------------
# Example: ChaiOrder with Multiple Constructors
# ------------------------------------

class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        # Instance attributes
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        """
        Create a ChaiOrder object from a dictionary.
        """
        return cls(order_data["tea_type"], order_data["sweetness"], order_data["size"])

    @classmethod
    def from_string(cls, order_string):
        """
        Create a ChaiOrder object from a comma-separated string.
        Format: 'tea_type,sweetness,size'
        """
        tea_type, sweetness, size = order_string.split(",")
        return cls(tea_type, float(sweetness), size)


# Creating instances using different constructors
order1 = ChaiOrder.from_dict({"tea_type": "Masala", "sweetness": 5, "size": "xl"})
order2 = ChaiOrder.from_string("Ice,2.5,small")
order3 = ChaiOrder("Lemon", 4.5, "large")

# Displaying instance data
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)

"""
Output:
{'tea_type': 'Masala', 'sweetness': 5, 'size': 'xl'}
{'tea_type': 'Ice', 'sweetness': 2.5, 'size': 'small'}
{'tea_type': 'Lemon', 'sweetness': 4.5, 'size': 'large'}
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- `@classmethod` methods operate on the class, not instances.
- Use `cls` as the first argument.
- Perfect for creating **alternative constructors** like:
  → from_dict(), from_string(), from_json(), etc.
- Called using ClassName.method_name().
"""