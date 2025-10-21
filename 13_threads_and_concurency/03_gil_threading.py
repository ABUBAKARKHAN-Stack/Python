# ------------------------------------
# 🧩 Global Interpreter Lock (GIL) in Python
# ------------------------------------

"""
? What is GIL
The Global Interpreter Lock (GIL) ensures that only ONE thread executes Python bytecode at a time,
even if you have multiple CPU cores.

👉 Meaning:
Threads in Python are not truly parallel for CPU-bound tasks because of the GIL.
They only appear concurrent due to context switching.

✅ GIL helps for I/O-bound tasks (like reading files or API calls)
❌ GIL slows down CPU-bound tasks (like loops and calculations)
"""

import threading
import time


# ------------------------------------
# Function: Simulating Baristas Brewing Chai ☕
# ------------------------------------
def brew_chai():
    print(f"{threading.current_thread().name} started the brewing process...")
    count = 0
    for _ in range(100_000):  # CPU-heavy loop (represents brewing effort)
        count += 1
    print(f"{threading.current_thread().name} finished the brewing process...")


# Creating two threads (two baristas)
thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

# Start timer
start = time.time()

# Start both threads
thread1.start()
thread2.start()

# Wait for both to complete
thread1.join()
thread2.join()

# End timer
end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")


# ------------------------------------
# 🧠 Observation:
# Even though we created two threads, total time doesn’t reduce much
# because GIL prevents both threads from running simultaneously.
# ------------------------------------

# ✅ Final Summary:
# - GIL allows only one thread to run Python code at a time.
# - Threads → good for I/O-bound tasks.
# - Multiprocessing → use this for CPU-heavy tasks to bypass GIL.
