# ------------------------------------
# Mini Project 2: Snack Suggestion System
# ------------------------------------

"""
📌 Concept:
In this project, we’ll create a simple snack suggestion program for a local café.
The café serves only **samosas** and **cookies**. If the customer orders either of these,
the order is confirmed. Otherwise, the program will politely decline.

🛠 Input in Python:
- We use the built-in input() function to take input from the user via CLI (Command Line).
- input() always returns data as a string.

Example:
user = input("Enter your name: ")
print(user)

On run:
Enter your name: Abubakar
Abubakar

⚠️ Problem:
User input can vary in letter case.
For example:
    - "SAMOSA"
    - "samosa"
    - "Samosa"
All of these should be treated the same, but Python sees them as different strings.

✅ Best Practice:
Convert the input to lowercase using the .lower() method.

Example:
user = input("Enter your name: ").lower()
# Now whether user types "ABUBAKAR" or "AbUbAkAr"
# The program always stores it as "abubakar".
"""

# Step 1: Take snack order input (always convert to lowercase for consistency)
snack = input("Enter your preferred snack: ").lower()

# Step 2: Conditional check for available snacks
if snack == "cookies" or snack == "samosa":
    print(f"✅ Great choice! We'll serve you: {snack}")
else:
    print("❌ Sorry, we only serve cookies or samosas with tea.")

"""
📝 Explanation:
- We first take input from the user and convert it to lowercase.
- Using an IF statement, we check if the entered snack matches "cookies" or "samosa".
- If yes → The order is confirmed.
- If not → The program informs the customer that the item is unavailable.

👉 This shows how IF-ELSE logic helps us control program flow based on user input.

⚡ Note: This is just another small touch on conditionals.
Next, we’ll explore ELSE-IF (elif) for multiple options. 🙂
"""