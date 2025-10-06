"""
@property Decorator in Python:
It allows us to define methods that can be accessed like attributes.
It’s used to control access (get, set) to instance variables while keeping syntax clean.
"""

class TeaLeaf:
    def __init__(self, age):
        # Convention: use _variable for private/internal use
        self._age = age

    # ───────────────────────────────
    # Getter → Access value safely
    @property
    def age(self):
        # Just an example: returning modified age (+2)
        # In real-world, return the actual value directly
        return self._age + 2

    # ───────────────────────────────
    # Setter → Control how value is updated
    @age.setter
    def age(self, age):
        # Simple validation logic for demonstration
        if 1 <= age <= 5:  # valid range 1–5
            self._age = age
        else:
            raise ValueError("❌ Tea Leaf Age Must be Between 1 and 5 Years.")

# ───────────────────────────────
# Creating object
leaf = TeaLeaf(2)
print("Initial age (with +2 logic):", leaf.age)

# Trying to set invalid value → will raise ValueError
leaf.age = 6
print("Updated age:", leaf.age)