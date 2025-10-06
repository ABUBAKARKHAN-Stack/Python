# ----------------------------
# Inheritance & Composition in Python
# ----------------------------

"""
? What is Inheritance
- Inheritance allows a class (child) to **reuse properties & methods** of another class (parent).
- It helps avoid code duplication and supports reusability.

👉 Key Points
- Parent class = Base / Superclass
- Child class = Derived / Subclass
- Child class can override or extend parent methods.

---

? What is Composition
- Composition = Building classes by **using other classes inside them** (has-a relationship).
- Example: A ChaiShop "has-a" Chai, rather than being a Chai itself.
- Promotes flexible design, where classes are combined like Lego blocks.
"""

# ----------------------------
# Example 1: Base Class
# ----------------------------
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")


# ----------------------------
# Example 2: Inheritance
# ----------------------------
class MasalaChai(BaseChai):  # Child class inherits BaseChai
    def add_spices(self):
        print("Adding cardamom, ginger, and cloves.")


# ----------------------------
# Example 3: Composition
# ----------------------------
class ChaiShop:
    chai_cls = BaseChai  # default chai type

    def __init__(self):
        # Shop contains a Chai (composition: has-a relationship)
        self.chai = self.chai_cls("Lemon")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()


# ----------------------------
# Example 4: Fancy Shop (Inheritance + Composition)
# ----------------------------
class FancyChaiShop(ChaiShop):  # Inherits from ChaiShop
    chai_cls = MasalaChai  # overrides chai_cls with MasalaChai


# ----------------------------
# Running the Code
# ----------------------------
shop = ChaiShop()
shop.serve()

fancy = FancyChaiShop()
fancy.chai.add_spices()


# ----------------------------
# Expected Output
# ----------------------------
"""
Serving Lemon chai in the shop
Preparing Lemon chai....
Adding cardamom, ginger, and cloves.
"""

# ----------------------------
# ✅ Final Notes
# ----------------------------
"""
- Inheritance → Child class extends or overrides behavior of parent.
- Composition → A class contains another class (has-a).
- Both can be used together for clean, modular, reusable code.
"""