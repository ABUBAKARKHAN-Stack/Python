# ------------------------------------
# Dictionary Comprehensions in Python
# ------------------------------------

"""
? What are Dictionary Comprehensions
Dictionary comprehensions are a **concise way** of creating dictionaries in Python using just a single line of code.
They make code **cleaner**, **shorter**, and bring logic in one place instead of writing long loops.

General Syntax:
    {key_expression: value_expression for item in iterable if condition}

👉 Note:
- You can use conditions (`if`) to filter elements.
- Variable names inside comprehension must be consistent with loop variables.
- You can also use multiple `for` loops.
- Dictionary stores data as **key-value pairs**.

Why use Dictionary Comprehensions?
- Cleaner code ✨
- Centralized logic in one line ⚡
- Works great for **transforming** or **filtering** dictionaries 📊
- Same result with fewer lines 🧹
"""

# ------------------------------------
# Example 1: Currency Conversion
# ------------------------------------

tea_prices_in_pkr = {"Masala Chai": 120, "Lemon Tea": 50, "Milk Chai": 70}

# Convert PKR prices to INR (approx 1 INR = 4 PKR)
tea_prices_in_inr = {tea: price / 4 for tea, price in tea_prices_in_pkr.items()}
print("Tea prices in INR:", tea_prices_in_inr)

"""
Output:
Tea prices in INR: {'Masala Chai': 30.0, 'Lemon Tea': 12.5, 'Milk Chai': 17.5}
"""

# ------------------------------------
# Example 2: Filtering Expensive Teas
# ------------------------------------

# Keep only teas priced above 100 PKR
expensive_teas = {tea: price for tea, price in tea_prices_in_pkr.items() if price > 100}
print("Expensive Teas:", expensive_teas)

"""
Output:
Expensive Teas: {'Masala Chai': 120}
"""

# ------------------------------------
# Example 3: Word Count Dictionary
# ------------------------------------

sentence = "chai is love and chai is life"
word_count = {word: sentence.split(" ").count(word) for word in sentence.split(" ")}
print("Word Count:", word_count)

"""
Output:
Word Count: {'chai': 2, 'is': 2, 'love': 1, 'and': 1, 'life': 1}
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- Dictionary comprehensions are used to create dictionaries in one line.
- Syntax: {key: value for item in iterable if condition}.
- Useful for **transforming**, **filtering**, or building dictionaries quickly.
- Much shorter and cleaner than traditional loops.

⚡ Next: We’ll explore **Generator Comprehensions**.
"""
