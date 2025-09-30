# ------------------------------------
# Logging (Project) with Decorators in Python
# ------------------------------------

"""
? What is Logging with Decorators
Logging is the process of **tracking function calls** and recording 
useful information like function name, parameters, and execution flow.  

Instead of writing print statements inside every function,  
we can use **decorators** to automatically log activity for any function.  

👉 Why use Logging Decorators?
- Cleaner code (no repetitive print statements in each function).
- Centralized logging logic ⚡
- Helps in debugging and tracking execution flow 🕵️‍♂️

---

? functools.wraps
- Used to preserve original function details (name, docstring).
- Without `@wraps`, the decorated function loses its identity.

---

✅ General Syntax for Logging Decorator:

from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper
"""

# ------------------------------------
# Example 1: Logging a Chai Function
# ------------------------------------

from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"👉 Calling: {func.__name__}")  # log before function runs
        result = func(*args, **kwargs)        # run original function
        print(f"✅ Finished: {func.__name__}") # log after function runs
        return result
    return wrapper


@log_activity
def brew_chai(type, milk="no"):
    """Simulates brewing chai"""
    print(f"Brewing {type} chai | Milk: {milk}")


brew_chai("Masala", "yes")

"""
Output:
👉 Calling: brew_chai
Brewing Masala chai | Milk: yes
✅ Finished: brew_chai
"""

# ------------------------------------
# Example 2: Logging Multiple Functions
# ------------------------------------

@log_activity
def take_order(customer, chai_type):
    print(f"{customer} ordered {chai_type}")


@log_activity
def serve_chai(cup_no):
    print(f"Serving chai cup #{cup_no}")


take_order("Ali", "Green Tea")
serve_chai(2)

"""
Output:
👉 Calling: take_order
Ali ordered Green Tea
✅ Finished: take_order

👉 Calling: serve_chai
Serving chai cup #2
✅ Finished: serve_chai
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- Logging decorators help track function calls and execution.
- Use @wraps to preserve original function identity.
- Useful for debugging, monitoring, and auditing function activity.
- Centralizes logging logic → less repetitive code and cleaner programs.
"""