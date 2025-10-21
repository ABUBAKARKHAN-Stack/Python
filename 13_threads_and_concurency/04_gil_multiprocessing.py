# ------------------------------------
# ⚙️ Multiprocessing in Python — Bypassing GIL
# ------------------------------------

"""
? What is Multiprocessing

The multiprocessing module allows the execution of multiple processes simultaneously.
Each process runs in its **own Python interpreter and memory space**,
which means they are **not limited by the Global Interpreter Lock (GIL)**.

✅ Ideal for CPU-bound tasks (e.g., heavy calculations, loops, data crunching)
❌ Slower startup time and higher memory usage than threading

👉 Each process runs independently and in parallel on multiple CPU cores.
"""

from multiprocessing import Process
import time


# ------------------------------------
# Function: Simulating Heavy Computation
# ------------------------------------
def crunch_number():
    print("Started the count process...")
    count = 0
    for _ in range(100_000_000):  # CPU-intensive task
        count += 1
    print("Ended the count process...")


# ------------------------------------
# Main Program Entry
# ------------------------------------
if __name__ == "__main__":
    start = time.time()

    # Create two separate processes (run truly in parallel)
    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    end = time.time()
    print(f"Total time with multiprocessing is {end - start:.2f} seconds")


# ------------------------------------
# 🧠 Observation:
# Unlike threads, processes bypass the GIL — both can run simultaneously.
# So, the total execution time reduces significantly on multi-core CPUs.
# ------------------------------------

# ✅ Final Summary:
# - Multiprocessing starts separate Python interpreters (not threads).
# - Each process runs independently, truly parallel.
# - Perfect for CPU-bound tasks like heavy loops or number crunching.
# - Comes with higher overhead (startup + memory) but better performance.