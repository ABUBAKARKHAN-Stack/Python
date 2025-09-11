# ------------------------------------
# Mini Project 1: Tea Stall Automation
# ------------------------------------

"""
📌 Concept:
We are building a small program for a tea stall that serves customers
holding tokens numbered from 1 to 10 and also prepares tea in multiple batches.  
Instead of writing multiple print statements, we’ll use a loop to repeat the task.

? What is a FOR loop?
A FOR loop in Python is used to iterate over a sequence (like numbers, lists, or strings).  
It repeats a block of code for each item in that sequence.

General Syntax:
for variable in range(start, stop):
    # code to execute for each iteration

Here, the sequence can be a range of numbers, a list, or any iterable object.
"""

# -------------------------------
# Task 1: Serving Tea by Tokens
# -------------------------------
for token in range(1, 11):   # range(1, 11) → generates numbers from 1 to 10
    print(f"☕ Serving Chai to token: #{token}")

# -------------------------------
# Task 2: Preparing Tea in Batches
# -------------------------------
for batch in range(1, 5):    # range(1, 5) → generates numbers from 1 to 4
    print(f"🍵 Preparing Chai for batch #{batch}")

"""
📝 Explanation:
- In Task 1:
  - We used range(1, 11) to generate numbers 1 through 10.
  - Each number represents a customer token.
  - The program prints a serving message for every token.

- In Task 2:
  - We used range(1, 5) to generate numbers 1 through 4.
  - Each number represents a batch of chai being prepared.
  - This shows how loops can be used for repetitive preparation tasks too.

👉 Key Point:
FOR loops are best used when the number of iterations is already known in advance.

⚡ Note: 
This is just the beginning of loops in Python.
We’ll explore while-loops, nested loops, and more real-world use cases very soon. 🙂
"""