# ------------------------------------
# Functions: Scopes in Python
# ------------------------------------

"""
? What are Function Scopes
Function scope defines the accessibility (visibility) of variables inside and outside functions.  

For example:  
If we have a variable `chai_type` inside a function and another one with the same name outside the function,  
then the one inside the function does not know about the outside one (and vice versa).  

Example:
    def print_order():
        chai_type = "Ice"
        print(chai_type)

    chai_type = "Lemon"
    print(chai_type)

👉 The variable `chai_type` inside the function is **local**, while the one outside is **global**.

📌 Types of Scopes in Python (LEGB Rule):
1. **Local Scope** → variables created inside a function.  
2. **Enclosing Scope** → variables in the outer function (when we have nested functions).  
3. **Global Scope** → variables declared outside any function.  
4. **Built-in Scope** → reserved names in Python (like `len`, `print`, etc.).  

⚡ Python always searches variables in this order:  
Local → Enclosing → Global → Built-in (LEGB Rule)
"""


# -------------------------------
# Local Scope
# -------------------------------
"""
Local Scope:
Variables created inside a function are accessible ONLY within that function.  
They live temporarily and vanish once the function ends.
"""
def print_order():
    chai_type = "Ice"   # local variable
    print(f"Inside the function: {chai_type} tea")

chai_type = "Lemon"     # global variable
print_order()
print(f"Outside the function: {chai_type} tea")



# -------------------------------
# Enclosing Scope
# -------------------------------
"""
Enclosing Scope:
If we have a nested function (a function inside another function),  
then the inner function can access variables of the outer function.  
This is also called **nonlocal scope**.
"""
def cafe_counter():
    order_bill = 1200   # enclosing variable (outer function)
    
    def print_bill():
        order_bill = 4000   # local variable (inner function)
        print(f"Order bill inside nested function (local scope): {order_bill}")
    
    print_bill()
    print(f"Order bill in enclosing function scope: {order_bill}")

order_bill = 4100   # global variable
cafe_counter()
print(f"Order bill in global scope: {order_bill}")



# -------------------------------
# Global Scope
# -------------------------------
"""
Global Scope:
Variables declared outside all functions are accessible everywhere in the file.  

If you want to modify a global variable inside a function,  
you must explicitly use the **global keyword**.  
"""
chai_flavor = "Masala"   # global variable

def update_chai():
    global chai_flavor
    chai_flavor = "Ginger"   # modifying global variable
    print(f"Inside function (after update): {chai_flavor} tea")

print(f"Before function call: {chai_flavor} tea")
update_chai()
print(f"After function call: {chai_flavor} tea")



# -------------------------------
# Built-in Scope
# -------------------------------
"""
Built-in Scope:
These are names reserved by Python itself (like `len`, `sum`, `print`, etc.).
You can use them anywhere without defining them.

⚠️ Warning: Avoid naming your variables same as built-ins,  
else it can shadow (overwrite) the original functionality.
"""
nums = [1, 2, 3, 4]
print(f"Length of nums list: {len(nums)}")  # built-in 'len'


# -------------------------------
# Final Summary
# -------------------------------
"""
✅ Local → Inside a function only.
✅ Enclosing → Outer function (when nested).
✅ Global → Declared at top level, accessible everywhere.
✅ Built-in → Predefined by Python (don’t overwrite them).

⚡ Order of search = LEGB Rule
"""