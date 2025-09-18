# ------------------------------------
# Functions: Basics in Python
# ------------------------------------

"""
? What are Functions
A function is a reusable block of code that performs a specific task.  
They are used to avoid writing repetitive code.  
The main goal of functions is **code reusability** and **modularity**.

General Syntax:
    def <function_name>(<parameters>):
        # body of function

Here:
- def → special keyword in Python to define a function.
- <function_name> → should be meaningful and well-named.
- (<parameters>) → optional inputs to pass dynamic data.

? Calling a Function
A function must be called after its definition to execute.  
If a function accepts parameters, we must pass arguments when calling it.

Example:
    def add(a, b):        # defining with parameters
        return a + b

    add(10, 20)           # calling with arguments

👉 Note:
- While defining → we use *parameters*.
- While calling → we pass *arguments*.

✅ Advantages of Functions:
- Write reusable code → reduce duplication.
- Break complex tasks into smaller, manageable parts.
- Organize code into modular units.
"""

# ------------------------------------
# Demonstration 1: Writing Reusable Code
# ------------------------------------

"""
Example:
A tea stall has many customers.  
Instead of writing multiple print statements,  
we create one function `print_order()` that takes two parameters (name, tea)  
and prints order details for different customers.
"""

def print_order(name, tea):
    print(f"{name} ordered {tea} tea.")

# Calling the function for multiple customers
print_order("Abubakar", "Black")
print_order("John", "Masala")
print_order("Ayesha", "Green")


# ------------------------------------
# Demonstration 2: Breaking Complex Tasks
# ------------------------------------

"""
Example:
We want to create a monthly report of a tea café’s sales.  
Instead of putting all the logic in one place,  
we divide it into smaller steps and call them inside a main function.

Steps:
1. fetch_sales()
2. filter_valid_orders()
3. summarize_data()
4. generate_report()  → calls all above functions
"""

def fetch_sales():
    print("📊 All sales fetched")

def filter_valid_orders():
    print("✅ Valid orders filtered")

def summarize_data():
    print("📃 A detailed summary of data created")

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()
    print("📑 Report generated successfully!")

# Calling the main function
generate_report()


# ------------------------------------
# Final Summary
# ------------------------------------
"""
✅ Functions are reusable blocks of code for specific tasks.  
✅ They make programs cleaner, modular, and easier to maintain.  
✅ They help break complex logic into smaller, simple steps.  
✅ While defining → we use *parameters*, while calling → we pass *arguments*.  

⚡ Note:
We’ll explore **Parameters & Arguments** in detail inside the `parameters_and_arguments` folder.
"""