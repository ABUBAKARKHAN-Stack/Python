# ------------------------------------
# Mini Project 2: Tea Token Queue System
# ------------------------------------

"""
📌 Concept:
We are building a simple system for a tea stall that serves customers in a queue.  
Each customer has a token number (or name). The stall serves them one by one until the queue is empty.

? Why While Loop?
A WHILE loop is useful when we don’t know exactly how many times the loop will run.  
It keeps running as long as the given condition is True.

General Syntax:
while condition:
    # code to execute
"""

# List of customers waiting for tea
tokens = ["Jhon", "Alex", "Mira", "Abubakar"]

# Serve customers until queue is empty
while tokens:   # loop continues as long as the list is not empty
    customer = tokens.pop(0)   # removes the first customer from the list
    print(f"☕ Serving tea to {customer}")


"""
📝 Explanation:
- We defined a list 'tokens' with customer names.
- The WHILE loop runs as long as 'tokens' is not empty (non-empty lists are considered True in Python).
- On each iteration, the first customer is removed using pop(0), and served.
- The loop stops automatically when the list becomes empty.

👉 Key Point:
- WHILE loops are perfect for situations where the number of iterations depends on a condition (not fixed).
- In this case, the condition is "queue not empty".

⚡ Note:
This is just a simple simulation.
You can extend it by adding conditions like:
- Stop serving if cups run out.
- Add new customers dynamically while serving.
"""