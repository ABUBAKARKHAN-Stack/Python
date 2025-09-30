# ------------------------------------
# Authorization with Decorators in Python
# ------------------------------------

"""
? What is Authorization
Authorization is the process of **restricting access** to certain functions 
or resources based on the user's role or permissions.  

For example:
- Only admins should be able to **access the tea inventory**.
- Normal users can’t see or modify it.

👉 Why use Authorization Decorators?
- Centralized access control (rules in one place).
- Cleaner code (no repeating `if role != admin` everywhere).
- Secure applications 🔐

---

? functools.wraps
- Used to keep the original function’s name and docstring.
- Without it, the function identity is lost after decoration.

---

✅ General Syntax for Authorization Decorator:

from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(role):
        if role != "admin":
            print("Access Denied: Admins Only")
            return None
        return func(role)
    return wrapper
"""

# ------------------------------------
# Example: Tea Inventory Access
# ------------------------------------

from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(userRole):
        if userRole != "admin":
            print("❌ Access Denied: Admins Only")
            return None  # Recommended: stops unauthorized access
        else:
            return func(userRole)
    return wrapper


@require_admin
def access_tea_inventory(role):
    """Function that simulates accessing tea inventory"""
    print("✅ Access Granted → Tea inventory opened!")


# Testing
access_tea_inventory("user")   # Unauthorized
access_tea_inventory("admin")  # Authorized

"""
Output:
❌ Access Denied: Admins Only
✅ Access Granted → Tea inventory opened!
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- Authorization decorators help control which roles can access functions.
- Use them to protect sensitive operations (like admin-only features).
- Cleaner and more secure than checking role inside every function.
- Example: Only 'admin' role can access the tea inventory.
"""