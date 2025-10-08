# Exceptions in Python (Intro)

"""
? What are Exceptions
Exceptions occur when there’s an error in our code, but instead of crashing the whole program, 
we can handle those errors gracefully.

Exceptions are useful because they allow us to:
✅ Detect problems
✅ Respond properly (without breaking the flow)
✅ Keep the application running

Some common built-in exceptions:
- IndexError
- ValueError
- TypeError
- KeyError
- ZeroDivisionError
and many more...

No one remembers them all — 
the key is to handle them gracefully!
"""

# Example: IndexError
orders = ["masala", "ginger"]
print(orders[2])  # ❌ IndexError: list index out of range