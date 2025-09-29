# ------------------------------------
# Infinite Generators in Python
# ------------------------------------

"""
? What are Infinite Generators
Infinite generators are generators that **never end** because they use an infinite loop (`while True`).  
They keep producing values endlessly until we explicitly stop them.  

👉 Why use Infinite Generators?
- Useful when you want a continuous data stream.
- Great for simulations, refills, counters, or data pipelines.
- More memory efficient than creating an infinite list (which is impossible).

⚡ But remember:
- You must control them with conditions, `break`, or limited iteration (otherwise they run forever).
"""

# ------------------------------------
# Example 1: Infinite Chai Refills
# ------------------------------------

def infinite_chai():
    count = 1
    while True:  # infinite loop → keeps generating
        yield f"Refill #{count}"
        count += 1


# User 1 Refills
refill = infinite_chai()

for _ in range(5):  # limit to 5 refills
    print(next(refill))

"""
Output:
Refill #1
Refill #2
Refill #3
Refill #4
Refill #5
"""

# ------------------------------------
# Example 2: Separate User Refill Streams
# ------------------------------------

"""
Each time we call the generator function, a new generator object is created.  
That means every user can have their **own infinite stream** of chai refills.
"""

user2 = infinite_chai()

for _ in range(6):  # limit to 6 refills
    print(next(user2))

"""
Output:
Refill #1
Refill #2
Refill #3
Refill #4
Refill #5
Refill #6
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- Infinite generators are created using `while True` inside a generator function.
- They produce endless values lazily (one at a time).
- Always control them with conditions or loops to avoid infinite execution.
- Use cases:
  - Continuous counters
  - Streaming data
"""