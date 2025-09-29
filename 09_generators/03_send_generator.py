# ------------------------------------
# Sending Values to Generators in Python
# ------------------------------------

"""
? What is send() in generators
Normally, generators only **yield values out**.  
But with the `.send(value)` method, we can also **send values INTO the generator** while it’s running.  

👉 How it works:
1. First, we start the generator with `next()` → it runs until the first `yield`.
2. After that, we can use `generator.send(value)` to:
   - Pass a value inside the generator
   - Resume execution from the last `yield`
   - Replace the `yield` expression with the sent value

⚡ Use Case:
- Great for real-time systems like order-taking, messaging, or pipelines.
"""

# ------------------------------------
# Example: Chai Stall Taking Orders
# ------------------------------------

def chai_customer():
    print("Welcome! What chai would you like?")
    order = yield  # first yield → waits for the order
    while True:
        print(f"Preparing {order} ☕")
        order = yield  # waits for the next order


# Create generator (chai stall)
stall = chai_customer()

# Step 1: Start generator (moves to first yield)
next(stall)

# Step 2: Send orders into the generator
stall.send("Masala Chai")
stall.send("Lemon Chai")
stall.send("Ginger Tea")

"""
Output:
Welcome! What chai would you like?
Preparing Masala Chai ☕
Preparing Lemon Chai ☕
Preparing Ginger Tea ☕
"""

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- Generators can also receive values with `.send(value)`.
- First call MUST be `next()` to move generator to first yield.
- After that, each `.send(value)` injects data into the generator.
- Use cases:
  - Live order systems
  - Real-time messaging
  - Event-driven pipelines
"""