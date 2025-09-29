# ------------------------------------
# List Comprehensions in Python
# ------------------------------------

"""
? What are List Comprehensions
List comprehensions are a **concise way** of creating lists in Python using just a single line of code.  
They make code **cleaner**, **shorter**, and bring logic in one place instead of writing long loops.

General Syntax:
    [expression for item in iterable if condition]

👉 Note:
- You can use conditions (`if`) to filter elements.
- Variable names inside comprehension must be consistent with loop variables.

Why use List Comprehensions?
- Cleaner code ✨
- Centralized logic in one line ⚡
- Same result with fewer lines 🧹
"""

# ------------------------------------
# Example 1: Traditional Way vs List Comprehension
# ------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional way → filter even numbers
even_nums = []
for n in numbers:
    if n % 2 == 0:
        even_nums.append(n)
print("Traditional way:", even_nums)

# Using list comprehension
even_nums = [n for n in numbers if n % 2 == 0]
print("List comprehension:", even_nums)

"""
Output:
Traditional way: [2, 4, 6, 8, 10]
List comprehension: [2, 4, 6, 8, 10]
"""

# ------------------------------------
# Example 2: Real-World Tea Menu Filtering
# ------------------------------------

"""
We have a tea menu and want to extract only teas that start with "Iced".
This is a **filtering use case** for list comprehensions.
"""

menu = ["Lemon Tea", "Masala Tea", "Iced Lemon Tea", "Ginger Tea", "Iced Peach Tea"]

iced_teas = [tea for tea in menu if "Iced" in tea]
print("Iced teas:", iced_teas)

"""
Output:
['Iced Lemon Tea', 'Iced Peach Tea']
"""

# ------------------------------------
# Example 3: Filtering Sales Data (Dictionaries)
# ------------------------------------

"""
We have today's sales data.  
We want to extract only the sales where the bill is greater than 2000.
"""

today_sales = [
    {"ordered_items": 10, "bill": 1900},
    {"ordered_items": 11, "bill": 2300},
    {"ordered_items": 50, "bill": 8000},
    {"ordered_items": 11, "bill": 1960},
]

today_highest_sales = [sale for sale in today_sales if sale["bill"] > 2000]
print("High sales:", today_highest_sales)

"""
Output:
[{'ordered_items': 11, 'bill': 2300}, {'ordered_items': 50, 'bill': 8000}]
"""

# ------------------------------------
# Example 4: Transforming Data
# ------------------------------------

"""
We have a list of orders.  
We want to **add 5% GST** to each bill using list comprehensions.
"""

orders = [
    {"items": 5, "bill": 250},
    {"items": 4, "bill": 200}
]

orders_with_gst = [
    {"items": order["items"], "final_bill": order["bill"] + (order["bill"] * 0.05)}
    for order in orders
]

print("Orders with GST applied:", orders_with_gst)

"""
Output:
Orders with GST applied:
[{'items': 5, 'final_bill': 262.5}, {'items': 4, 'final_bill': 210.0}]
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- List comprehensions are used to create lists in one line.
- Syntax: [expression for item in iterable if condition].
- They help in **filtering** and **transforming** data quickly.
- Much shorter and cleaner than traditional loops.

⚡ Next: We’ll explore **Set Comprehensions**.
"""