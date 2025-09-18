# ------------------------------------
# Functions 02: nonlocal vs global in Python
# ------------------------------------

"""
? What are nonlocal and global keywords in functions
Both are used inside functions to access and override variables,  
but they work differently depending on where the variable lives.
"""

# -------------------------------
# nonlocal
# -------------------------------
"""
👉 nonlocal:
- Used when we have a nested function (a function inside another function).
- It connects the variable of the inner function to the variable of the outer function.
- The scope of this remains only between those two functions, not global.

Syntax:
    nonlocal <variable_name>
"""

# Without using nonlocal
def update_order_no_nonlocal():
    chai_type = "Masala"

    def kitchen():
        chai_type = "Ice"
        print("Chai Type inside inner function:", chai_type)

    kitchen()
    print("Chai Type outside outer function:", chai_type)

update_order_no_nonlocal()

"""
Output:
Chai Type inside inner function: Ice
Chai Type outside outer function: Masala

💡 Why?  
Because both inner and outer function created their own chai_type.  
Each function has a separate scope.
"""


# With using nonlocal
def update_order_with_nonlocal():
    chai_type = "Masala"

    def kitchen():
        nonlocal chai_type
        chai_type = "Ice"
        print("Chai Type inside inner function:", chai_type)

    kitchen()
    print("Chai Type outside outer function:", chai_type)

update_order_with_nonlocal()

"""
Output:
Chai Type inside inner function: Ice
Chai Type outside outer function: Ice

💡 Why?  
Because `nonlocal` makes the inner function directly point to the outer function’s variable.  
So when we changed it inside, the outer also got updated.
"""


# -------------------------------
# global
# -------------------------------
"""
👉 global:
- Used when we want to connect our function variable to a variable declared outside of all functions.
- With `global`, we can update or create variables in the global scope.
- Be careful, because it changes the value everywhere in the program.

Syntax:
    global <variable_name>
"""

# Without using global
chai_flavor = "Lemon"

def kitchen_no_global():
    chai_flavor = "Masala"   # this is a local variable, not touching global
    print("Inside function:", chai_flavor)

kitchen_no_global()
print("Outside function:", chai_flavor)

"""
Output:
Inside function: Masala
Outside function: Lemon

💡 Why?  
The function created its own local variable instead of changing the global one.
"""


# With using global
chai_flavor = "Lemon"

def kitchen_with_global():
    global chai_flavor
    chai_flavor = "Masala"   # now this updates the global variable
    print("Inside function:", chai_flavor)

kitchen_with_global()
print("Outside function:", chai_flavor)

"""
Output:
Inside function: Masala
Outside function: Masala

💡 Why?  
Because we used `global`, the function directly updated the global variable.
"""


# -------------------------------
# Final Summary
# -------------------------------
"""
✅ nonlocal → inner function variable connects to outer function variable.  
✅ global   → function variable connects to global variable.  

⚡ Rule of Thumb:
- Use **nonlocal** when working with nested functions.  
- Use **global** when you want to affect variables outside all functions.  
"""