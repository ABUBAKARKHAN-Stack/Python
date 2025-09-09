# ------------------------------------
# Mini Project 5: Delivery Fee Waiver
# ------------------------------------

"""
📌 Concept:
In this project, we’ll simulate a café’s delivery fee system.

The rule:
- If the order amount is more than 300 → Delivery is FREE.
- Otherwise → Delivery fee is 30 Rupees.

? Why Ternary Operator?
- Normally, we would use if/else for this:
    if order_amount > 300:
        delivery_fee = 0
    else:
        delivery_fee = 30

- But this is short and repetitive.
- With a **ternary operator**, we can write it all in one line → cleaner & more Pythonic.

⚡ General Syntax:
    <value_if_true> if <condition> else <value_if_false>

🛠 Input Reminder:
- input() always returns a string.
- We wrap it with int() because order amount should be a number.
"""

# Step 1: Take user input (order amount)
order_amount = int(input("Enter Order Amount: "))

# Step 2: Apply ternary operator for delivery fee
delivery_fee = 0 if order_amount > 300 else 30

# Step 3: Show result
print(f"Delivery Fee: {delivery_fee} Rupees")

"""
📝 Explanation:
- If order_amount > 300 → fee = 0.
- Else → fee = 30.
- Much shorter and easier to read than writing full if/else block.

👉 This is just a small touch into Python’s **ternary operator**,
which is great for simple one-line conditions.
"""
