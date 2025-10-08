# ------------------------------------
# Try Except Error Handling in Python
# ------------------------------------

"""
? What is try-except-finally

In Python, we use `try-except` blocks to handle runtime errors gracefully
— this ensures our program doesn’t crash unexpectedly.

✅ try       → Code that might raise an error  
✅ except    → Executes only if an error occurs  
✅ else      → Executes only if NO error occurs  
✅ finally   → Always executes (cleanup or message)
"""

# ------------------------------------
# Example 1: Basic try-except
# ------------------------------------

chai_menu = {"masala": 30, "ginger": 50}

# ❌ This would raise KeyError and crash
# chai_menu["elaichi"]
# print("Hello") # This never runs if above fails

# ✅ Handle gracefully using try-except
try:
    chai_menu["elaichi"]
except KeyError:
    print("The key you are trying to access does not exist!")

print("Hello")  # ✔ Runs even after exception


# ------------------------------------
# Example 2: Full try-except-else-finally
# ------------------------------------

def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor!")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"{flavor} chai is served successfully ☕")
    finally:
        print("Next customer please!\n")


serve_chai("masala")
serve_chai("unknown")


# ------------------------------------
# 🧾 Output:
# ------------------------------------
"""
The key you are trying to access does not exist!
Hello
Preparing masala chai...
masala chai is served successfully ☕
Next customer please!

Preparing unknown chai...
Error: We don't know that flavor!
Next customer please!
"""

# ------------------------------------
# ✅ Final Summary:
# ------------------------------------
"""
- try → Block of code that might cause an error.
- except → Handles specific or general exceptions.
- else → Runs only if try succeeds (no errors).
- finally → Always executes (useful for cleanup).
- This structure helps prevent full program crashes and 
  ensures smooth error recovery.
"""