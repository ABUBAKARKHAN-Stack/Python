# ------------------------------------
# Mini Project 2: Tea Order Notifier
# ------------------------------------

"""
📌 Concept:
We are creating a small system for a café that notifies customers 
when their tea orders are ready.  

Instead of printing separate messages for each customer, 
we’ll use a FOR-IN loop to iterate through a list of names and notify them one by one.

? What is a FOR-IN loop with Lists?
- A list in Python is an ordered collection of items (strings, numbers, etc.).
- A FOR-IN loop is commonly used to go through each item in the list one by one.
- On each iteration, the current item is stored in a temporary variable, 
  which can then be used inside the loop.

General Syntax (Lists):
for variable in list_name:
    # code to execute for each element
"""

# List of customer names
names = ["Jhon", "Alex", "George"]

# Loop through names and print notifications
for name in names:   # 'name' takes each value from the list one by one
    print(f"✅ Order is ready for: {name}")


"""
📝 Explanation:
- We created a list called 'names' containing customer names.
- The FOR-IN loop iterates through this list, assigning each element to the variable 'name'.
- For every customer, the program prints a message that their order is ready.

👉 Key Point:
- Lists store multiple values, and the FOR-IN loop helps us process each value easily.
- This avoids repetitive code and makes the program scalable.  
  (If the list had 100 names, the same loop would still work without changes!)

⚡ Extra Tip: Using FOR-IN with Dictionaries
- We can also use the FOR-IN loop with dictionaries.  
- In that case:
    - Looping directly gives us the keys.
    - We can use `.items()` to get both key and value.

Example:
orders = {"Jhon": "Masala Chai", "Alex": "Green Tea", "George": "Lemon Tea"}

for customer, tea in orders.items():
    print(f"✅ {customer}, your {tea} is ready!")

⚡ Note:
This is just the beginning of working with lists (and dictionaries) inside loops.  
Later, we’ll explore nested loops, conditions inside loops, and more practical use cases. 🙂
"""