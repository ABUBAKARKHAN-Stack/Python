# ------------------------------------
# Mini Project 3: Cup Size Price Calculator
# ------------------------------------

"""
📌 Concept:
In this project, we’ll create a simple program for a café that asks the customer 
to choose their cup size and then displays the price accordingly.

? Why Elif?
- If we only used IF + ELSE, we would have to nest multiple conditions, making the code messy.
- With ELIF (else if), we can check multiple options in a clean way.

🛠 Input Reminder:
- input() always returns a string.
- To make comparisons easier, we use .lower() so case differences won’t break the program.
"""

# Step 1: Ask customer for their cup size
cup_size = input("Choose your cup size (small | medium | large): ").lower()

# Step 2: Conditional checks for pricing
if cup_size == "large":
    print("💰 Price is 20 rupees")
elif cup_size == "medium":
    print("💰 Price is 15 rupees")
elif cup_size == "small":
    print("💰 Price is 10 rupees")
else:
    print("❌ Unknown cup size :(")

"""
📝 Explanation:
- The program takes input from the user and converts it to lowercase.
- IF checks if the size is "large".
- ELIF checks for "medium".
- Another ELIF checks for "small".
- ELSE acts as a catch-all if none of the above match (invalid input).

👉 This project is a practical use of IF-ELIF-ELSE for handling multiple choices.
It feels like building a **mini vending machine** logic!
"""
