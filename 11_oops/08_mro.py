# ------------------------------------
# Method Resolution Order (MRO) in Python
# ------------------------------------

"""
? What is MRO
MRO (Method Resolution Order) defines the **order in which Python looks for
attributes or methods** when multiple inheritance is involved.

👉 In simple words:
When you access an attribute or method on an object,
Python follows a **search path** to find it — from **child → parent(s) → object**.

MRO decides which class is checked first, second, and so on.

---

🧩 Why It’s Important:
- Helps Python know **which parent class to use first** when multiple are inherited.
- Avoids confusion and conflicts in **diamond inheritance** situations.
- Keeps the lookup predictable and consistent.

---
"""

# ------------------------------------
# Example: Multiple Inheritance
# ------------------------------------
class A:
    label = "A: Base class"


class B(A):
    label = "B: Masala blend"


class C(A):
    label = "C: Herbal blend"


# D inherits from C and B
class D(C, B):  # 👈 If you change order to (B, C), output changes!
    pass


# Creating an instance
cup = D()

print(cup.label)  # Output → ?

"""
👉 Explanation:
Python will search for `label` in the following order:
    D → C → B → A → object

Since `C` comes before `B` in the inheritance list,
Python picks `C.label` first.
"""

# ------------------------------------
# 🔍 Checking the MRO order explicitly
# ------------------------------------
print(D.mro())   # or use help(D)

"""
Output:
[
  <class '__main__.D'>,
  <class '__main__.C'>,
  <class '__main__.B'>,
  <class '__main__.A'>,
  <class 'object'>
]

So Python looks up attributes in this exact sequence.
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- MRO = the path Python follows to find methods/attributes.
- In multiple inheritance:
    Leftmost base class is searched first.
- Use `ClassName.mro()` or `help(ClassName)` to inspect MRO.
- It ensures **consistent, predictable** attribute/method lookup order.
"""