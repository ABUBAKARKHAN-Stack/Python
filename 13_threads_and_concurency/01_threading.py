# ------------------------------------
# Concurrency in Python 🧵
# ------------------------------------

"""
? What is Concurrency
Concurrency means performing **multiple tasks at the same time** — not truly parallel,
but by switching rapidly between them.

For example 👇
You are **making chai** while **chatting with your friend**.
You're not stopping one task completely — you're switching between both efficiently.

⚙️ Key Idea:
- Runs on a **single CPU core**.
- Uses **multiple threads** to perform tasks concurrently.
- Controlled using the built-in `threading` module.
"""

# ------------------------------------
# Syntax & Working Explanation
# ------------------------------------
"""
Step-by-step overview:

1️⃣ Import the threading module:
    import threading

2️⃣ Define multiple functions that perform different tasks.

3️⃣ Create threads for each function:
    thread1 = threading.Thread(target=func_one)
    thread2 = threading.Thread(target=func_two)

4️⃣ Start the threads using:
    thread1.start()
    thread2.start()

5️⃣ Use **join()** to make sure main program waits until all threads complete:
    thread1.join()
    thread2.join()

🧠 Without `.join()`, the program might exit before threads finish their work.
"""

# ------------------------------------
# Example: Tea Stall — Handling Orders & Brewing Together 🍵
# ------------------------------------

import threading
import time


# Simulate taking orders
def take_orders():
    for i in range(1, 4):
        print(f"🧾 Taking order for #{i}")
        time.sleep(2)  # Simulate time delay per order


# Simulate brewing chai
def brew_chai():
    for i in range(1, 4):
        print(f"☕ Brewing chai for #{i}")
        time.sleep(3)  # Brewing takes more time than taking order



# Create threads with target functions
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

# Start threads → both tasks run concurrently
order_thread.start()
brew_thread.start()

# Wait for both threads to complete before moving ahead
order_thread.join()
brew_thread.join()

# Final statement after both threads finish
print("✅ All orders are taken and chai brewed successfully!")


# ------------------------------------
# 🧾 Output Example:
# ------------------------------------
"""
🧾 Taking order for #1
☕ Brewing chai for #1
🧾 Taking order for #2
🧾 Taking order for #3
☕ Brewing chai for #2
☕ Brewing chai for #3
✅ All orders are taken and chai brewed successfully!
"""

# ------------------------------------
# ✅ Final Summary:
# ------------------------------------
"""
- **Concurrency** = multiple tasks switching rapidly on one core.
- **threading.Thread()** → creates thread for a function.
- **start()** → begins thread execution.
- **join()** → waits for threads to finish.
- Used for tasks like I/O operations, file reading, or API requests.

⚡ Helps improve responsiveness & efficiency without actual parallelism.
"""
