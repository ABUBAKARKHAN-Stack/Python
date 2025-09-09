# ------------------------------------
# Mini Project 1: Smart Kettle Notifier
# ------------------------------------

"""
📌 Concept:
We are creating a simple notification system for a smart kettle.
If the kettle is boiled, it should notify us by printing a message.
This is done using an IF statement in Python.

? What is an IF statement?
The IF statement allows us to make decisions in our code.
It checks a condition (True/False). If the condition is True, the block of code inside IF executes.
If it’s False, the block is skipped.

General Syntax:
if condition:
    # code to execute if condition is True
"""

# Variable to track the kettle status
is_kettle_boiled = True   # Boolean value → True means kettle is boiled, False means not yet

# IF statement to check the status
if is_kettle_boiled:
    print("✅ Kettle Boiled! Time To Make Chai.")

"""
📝 Explanation:
- We defined a variable is_kettle_boiled and set it to True.
- The IF statement checks the value of is_kettle_boiled.
- Since it’s True, the code inside IF runs and prints the notification.
- If is_kettle_boiled was False, nothing would happen.

👉 This is the foundation of conditionals in Python.
We’ll extend this later using ELSE and ELIF to handle more cases.

⚡ Note: This is just a small touch on the topic of IF statements.
We’ll explore deeper (else, elif, nested conditions) very soon. 🙂
"""