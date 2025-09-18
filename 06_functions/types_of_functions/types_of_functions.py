# ------------------------------------
# Functions: Types in Python
# ------------------------------------

"""
? Types of Functions in Python

Functions in Python can be categorized into different types:

1. Pure Functions
2. Impure Functions
3. Recursive Functions
4. Lambda (Anonymous) Functions
"""

# ------------------------------------
# 1. Pure Functions
# ------------------------------------
"""
A **pure function** always returns the same output for the same input  
and does not modify any external state.
"""


def pure_chai(cups):
    return cups * 10


print(pure_chai(30))  # Output: 300


# ------------------------------------
# 2. Impure Functions
# ------------------------------------
"""
An **impure function** may change external/global variables  
or depend on them. Its output can vary based on outside state.
"""

total_cups = 0


def impure_chai(cups):
    global total_cups
    total_cups += cups
    return total_cups


print(impure_chai(10))  # Output: 10
print(impure_chai(5))  # Output: 15


# ------------------------------------
# 3. Recursive Functions
# ------------------------------------
"""
A **recursive function** is a function that calls itself  
until a base condition is met.
"""


def pour_chai(n):
    if n == 0:
        print("✅ All chai poured")
        return
    print(f"Pouring chai cup {n}")
    return pour_chai(n - 1)


pour_chai(5)


# ------------------------------------
# 4. Lambda (Anonymous) Functions
# ------------------------------------
"""
? What are Lambda Functions

- **Lambda functions** are small, anonymous (nameless) functions.  
- They are often used in places where functions are required temporarily  
  (like `map`, `filter`, `sorted`).  
- They implicitly return values (no need for `return` keyword).  
- Written in **one line** using the `lambda` keyword.

Syntax:
    lambda <parameters>: <expression>

Example: 
add = lambda a, b: a + b
print(add(2, 3))  # Output: 5    
"""

# Example 1: Storing cups
cups = lambda cup: cup
print(cups(10))  # Output: 10

# Example 2: Using lambda in filter()
teas = ["Lemon", "Masala", "Lemon"]
filtered_tea = list(filter(lambda tea: tea.lower() != "lemon", teas))
print(filtered_tea)  # Output: ['Masala']

# Example 3: Using lambda in map()
sub_total = [100, 210, 102]
# add 2% GST on each bill
final_bill = list(map(lambda total: total + (total * 0.02), sub_total))
print(final_bill)  # Output: [102.0, 214.2, 104.04]

# Example 4: Using lambda in max()
yearly_sales = [
    {"year": 2021, "sale": 5000},
    {"year": 2022, "sale": 7000},
    {"year": 2023, "sale": 6500},
]
top_sale_year = max(yearly_sales, key=lambda s: s["sale"])
print(top_sale_year)  # Output: {'year': 2022, 'sale': 7000}


# ------------------------------------
# Final Summary
# ------------------------------------

"""
✅ **Pure Functions** → No side effects, same output for same input.  
✅ **Impure Functions** → Depend on or modify external state.  
✅ **Recursive Functions** → Call themselves until a base condition is met.  
✅ **Lambda Functions** → One-line, anonymous functions (useful with map, filter, sorted).  
"""
