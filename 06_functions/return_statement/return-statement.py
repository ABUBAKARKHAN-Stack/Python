# ------------------------------------
# Functions: Return Statement in Python
# ------------------------------------

"""
? What is return statement

The `return` statement is used to send values from a function back to the caller.

General Syntax:
def <function_name>(<values>):
    return <values>

👉 Key Points:
- A function can return **one** or **multiple** values.
- You can return **any datatype** (int, str, list, dict, tuple, etc.).
- If no return is used → Python returns `None` by default.
"""


# ------------------------------------
# Example 1: Returning One Value
# ------------------------------------
def make_chai(tea_name):
    return f"Here's your {tea_name} chai."


returned_value = make_chai("Masala")
print(returned_value)

"""
Output:
Here's your Masala chai.
"""


# ------------------------------------
# Example 2: Returning Multiple Values
# ------------------------------------
def chai_report():
    sold = 142
    remaining = 21
    return sold, remaining  # returns a tuple


sold, remaining = chai_report()
print("Sold:", sold)
print("Remaining:", remaining)

"""
Output:
Sold: 142
Remaining: 21
"""

# ------------------------------------
# Example 3: Early Return
# ------------------------------------
"""
We can use `return` to exit a function early.
"""


def chai_status(cups_left):
    if cups_left <= 0:
        return "❌ Sorry, cups are finished"
    return "✅ Chai is ready"


print(chai_status(0))
print(chai_status(5))

"""
Output:
❌ Sorry, cups are finished
✅ Chai is ready
"""

# ------------------------------------
# Final Summary
# ------------------------------------
"""
✅ `return` sends values from a function back to the caller.  
✅ If no `return` is given → function returns `None` by default.  
✅ Functions can return one or multiple values.  
✅ `return` can also be used for **early exit** from a function.  
"""
