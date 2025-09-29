# ------------------------------------
# Advanced Generators in Python
# ------------------------------------

"""
? What is `yield from`
Normally, if we want a generator to yield values from another generator,  
we must loop manually. But Python gives us `yield from` which:
- Delegates work to another generator
- Automatically yields all its values
- Makes code cleaner and shorter

? What is close() in generators
Generators can be stopped/cleaned up by calling `.close()`.  
- It raises a `GeneratorExit` exception inside the generator.  
- You can handle it (with try/except) to perform cleanup tasks.
"""

# ------------------------------------
# Example 1: Using `yield from`
# ------------------------------------

def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha Chai"
    yield "Oolong Chai"

def full_menu():
    # Delegate work → get values from both generators
    yield from local_chai()
    yield from imported_chai()

print("Full Menu:")
for chai in full_menu():
    print(chai)

"""
Output:
Full Menu:
Masala Chai
Ginger Chai
Matcha Chai
Oolong Chai
"""

# ------------------------------------
# Example 2: Using close() for Cleanup
# ------------------------------------

def chai_stall():
    try:
        while True:
            yield "Waiting for chai order..."
    except:  # raised when .close() is called
        print("Stall closed 🚫 No more chai.")

stall = chai_stall()

# First request
print(next(stall))

# Closing the generator → cleanup triggered
stall.close()

"""
Output:
Waiting for chai order...
Stall closed 🚫 No more chai.
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- `yield from` lets one generator yield values from another.
- `close()` gracefully stops a generator and allows cleanup.
- These features are useful for:
  - Combining multiple data sources
  - Resource cleanup (like closing DB connections, files, etc.)
"""