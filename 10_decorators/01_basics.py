# ------------------------------------
# Decorators in Python
# ------------------------------------

"""
? What are Decorators in Python
Decorators are **special functions** in Python that allow us to 
**add extra behavior** to another function **without modifying its code**.

Think of it like a chai stall:
- Customer orders chai (main function).
- Stall owner says "Welcome" before serving and "Thank you" after serving.
- That "extra work" before/after is done by the decorator.

👉 Key Points:
- Decorators take a function as input and return a new function.
- Implemented using **higher-order functions** (functions inside functions).
- Often used for logging, authentication, validation, or timing.
- Use the `@<decorator_name>` syntax for clean and easy usage.

---

? functools.wraps
- When we decorate, the original function’s metadata (like name, docstring) gets replaced.
- `@wraps(func)` is used to preserve the original function’s identity.

---

✅ General Syntax:

from functools import wraps

def <decorator_name>(func):
    @wraps(func)
    def wrapper():
        # Code before function runs
        func()
        # Code after function runs
    return wrapper

@<decorator_name>
def my_function():
    print("Main function work")

my_function()
"""

# ------------------------------------
# Example 1: Simple Decorator
# ------------------------------------

from functools import wraps

def my_decorator(func):
    @wraps(func)   # keeps original function's metadata safe
    def wrapper():
        print("Before function runs (Welcome!)")
        func()
        print("After function runs (Thank you!)")
    return wrapper


@my_decorator
def greet():
    print("Hello from decorated function (Serving chai...)")


greet()

"""
Output:
Before function runs (Welcome!)
Hello from decorated function (Serving chai...)
After function runs (Thank you!)
"""

# ------------------------------------
# Example 2: Checking Function Identity
# ------------------------------------

print(greet.__name__)  # greet (because of @wraps)

"""
Without @wraps:
print(greet.__name__)  --> wrapper
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- Decorators allow us to **wrap functions with extra behavior**.
- They use higher-order functions and the `@decorator` syntax.
- `@wraps` ensures original function details are preserved.
- Real-world use cases: logging, authentication, validation, measuring execution time, etc.
"""