# ------------------------------------
# Generator Comprehensions in Python
# ------------------------------------

"""
? What are Generator Comprehensions
Generator comprehensions are similar to list comprehensions but instead of
creating the entire list in memory, they generate items **one by one** (lazy evaluation).

General Syntax:
    (expression for item in iterable if condition)

👉 Note:
- Use **( )** instead of [ ].
- Generators don’t store all data in memory → more memory-efficient 💾.
- You can iterate over them or use functions like `sum()`, `max()`, `min()`.
"""

# ------------------------------------
# Example: Daily Tea Sales
# ------------------------------------

"""
We have daily tea sales (cups sold).  
We want the total number of cups sold where sales were greater than 5.
"""

daily_sales = [4, 5, 6, 5, 10, 13, 8, 3, 1, 30, 50]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print("Total cups (sales > 5):", total_cups)

"""
Output:
Total cups (sales > 5): 117
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- Generator comprehensions work like list comprehensions but don’t create the whole list.
- Syntax: (expression for item in iterable if condition).
- They are **faster** and **memory efficient** when dealing with large datasets.
- Great for cases where you don’t need to store all values, only process them.
"""
