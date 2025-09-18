# ------------------------------------
# Functions: Parameters and Arguments in Python
# ------------------------------------

"""
? What are Parameters
Parameters are special variables defined inside the parentheses of a function definition.
They act as **placeholders** that allow us to pass dynamic values to functions.

? What are Arguments
Arguments are the **actual values** we pass when calling a function.
They replace the placeholders (parameters) during execution.

👉 Important:
- While **defining** a function → we use *parameters*.
- While **calling** a function → we pass *arguments*.

General Syntax:
    def function_name(parameter1, parameter2, ...):
        # function body

    function_name(argument1, argument2, ...)
"""

# ------------------------------------
# Example 1: Function with Parameters and Arguments
# ------------------------------------


def print_tea_name(tea_name):  # 'tea_name' is a parameter
    print(f"{tea_name} chai.")


# Passing values while calling (arguments)
print_tea_name("Masala")
print_tea_name("Ice")
print_tea_name("Ginger")

"""
Output:
Masala chai.
Ice chai.
Ginger chai.
"""

# ------------------------------------
# Example 2: Multiple Parameters and Arguments
# ------------------------------------


def print_tea_order(tea, size):  # two parameters
    print(f"Tea: {tea} | Size: {size}")


# calling with arguments
print_tea_order("Ice", "Large")
print_tea_order("Ginger", "Medium")

"""
Output:
Tea: Ice | Size: Large
Tea: Ginger | Size: Medium
"""

# ------------------------------------
# Example 3: Real-Life Example
# ------------------------------------

"""
Imagine a tea stall:  
- Parameters act as placeholders (name, tea_type).  
- Arguments are actual values (like "Abubakar", "Green").  
"""


def print_order(name, tea_type):
    print(f"{name} ordered {tea_type} tea.")


# Different customers → same function
print_order("Abubakar", "Green")
print_order("Ayesha", "Black")
print_order("Ali", "Masala")

"""
Output:
Abubakar ordered Green tea.
Ayesha ordered Black tea.
Ali ordered Masala tea.
"""

# ------------------------------------
# Example 4: Parameters and Args in Complex Task
# ------------------------------------


def generate_report(month, sales):
    print(f"📑 Report for {month}: Total Sales = {sales}")


# Calling with different arguments
generate_report("January", 1200)
generate_report("February", 800)

"""
Output:
📑 Report for January: Total Sales = 1200
📑 Report for February: Total Sales = 800
"""

# ------------------------------------
# Example 5: Default Parameters
# ------------------------------------

"""
Sometimes we want parameters to have a default value.  
This way, if no argument is passed, the default one is used.
"""


def tea_recipe(liquid="Water", tea_type="Masala"):
    print(f"Boiling {liquid} for {tea_type} tea...")


# Calling with and without arguments
tea_recipe()
tea_recipe("Milk", "Ginger")

"""
Output:
Boiling Water for Masala tea...
Boiling Milk for Ginger tea...
"""

# ------------------------------------
# Types of Parameters and Arguments in Python
# ------------------------------------

"""
Python supports different types of parameters and arguments.
"""

# 1. Positional Parameters and Arguments
"""
Arguments are matched to parameters in the same order.
"""


def make_tea(tea_type, size):
    print(f"Making {size} {tea_type} tea...")


make_tea("Masala", "Large")  # order matters
make_tea("Green", "Small")

"""
Output:
Making Large Masala tea...
Making Small Green tea...
"""

# 2. Keyword Parameters and Arguments
"""
Arguments are passed with the parameter name → order does not matter.
"""

make_tea(size="Medium", tea_type="Ginger")
make_tea(tea_type="Lemon", size="Large")

"""
Output:
Making Medium Ginger tea...
Making Large Lemon tea...
"""

# 3. Default Parameters
"""
If no value is passed, the default value is used.
"""


def special_tea(tea_type="Elaichi", size="Regular"):
    print(f"Serving {size} {tea_type} tea...")


special_tea()  # uses defaults
special_tea("Masala")  # overrides tea_type
special_tea(size="Large")  # overrides size
special_tea("Green", "Extra Large")  # overrides both

"""
Output:
Serving Regular Elaichi tea...
Serving Regular Masala tea...
Serving Large Elaichi tea...
Serving Extra Large Green tea...
"""

# 4. Variable-Length Parameters and Arguments (*args)
"""
Sometimes we don’t know how many arguments will be passed.  
We use `*` before the parameter name → Python collects them into a tuple.
"""


def chai_recipe(chai_type, *ingredients):
    print(f"{chai_type} chai recipe: {ingredients}")


chai_recipe("Milk", "water", "milk", "tea leaves", "sugar", "cardamom (optional)")
chai_recipe("Lemon", "lemon", "grass tea", "water", "sugar")

"""
Output:
Milk chai recipe: ('water', 'milk', 'tea leaves', 'sugar', 'cardamom (optional)')
Lemon chai recipe: ('lemon', 'grass tea', 'water', 'sugar')
"""

# 5. Keyword Variable-Length Parameters and Arguments (**kwargs)
"""
If we want to pass multiple key-value arguments,  
we use `**` before the parameter name → Python collects them into a dictionary.
"""


def order_details(**order):
    print(order)


order_details(teas=["Ice", "Masala"], cup_size="Medium", totalAmount=400)

"""
Output: 
{'teas': ['Ice', 'Masala'], 'cup_size': 'Medium', 'totalAmount': 400}
"""

# ------------------------------------
# Final Summary
# ------------------------------------

"""
✅ Parameters are placeholders in a function definition.  
✅ Arguments are actual values passed while calling the function.  
✅ Types of Parameters/Arguments:
   1. Positional → order matters  
   2. Keyword → order doesn’t matter  
   3. Default → pre-set values, can be overridden  
   4. Variable-length (*args) → collects values into a tuple  
   5. Keyword Variable-length (**kwargs) → collects values into a dictionary  

✅ Together, they make functions flexible, reusable, and powerful.
"""
