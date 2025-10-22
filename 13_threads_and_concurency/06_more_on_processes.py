# ------------------------------------
# 🧵 More on Threads & Multiprocessing
# ------------------------------------

"""
🔥 Number Crunching Battle — Threads vs Processes (CPU-HEAVY TASKS)

We already know the winner 💪 (hint: multiprocessing),
but let's *see it in action* and understand **why** it's always preferred
for CPU-bound tasks.

Remember:
- Threading → good for I/O-bound (like API calls, file reads)
- Multiprocessing → best for CPU-heavy work (like loops, calculations)
"""

# ------------------------------------
# ⚙️ Threads Example — CPU Heavy Task (Slower due to GIL)
# ------------------------------------

# import threading
# import time
#
#
# def cpu_heavy():
#     print("Crunching some numbers...")
#     total = 0
#     for i in range(10**7):
#         total += i
#     print("Done!")
#
#
# start = time.time()
# threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
#
# # Start both threads
# [t.start() for t in threads]
#
# # Wait for both to finish
# [t.join() for t in threads]
#
# end = time.time()
#
# print(f"Time taken with THREADS: {end - start:.2f} seconds.")


# ------------------------------------
# ⚙️ Multiprocessing Example — CPU Heavy Task (Faster 🚀)
# ------------------------------------

# from multiprocessing import Process
# import time
#
#
# def cpu_heavy():
#     print("Crunching some numbers...")
#     total = 0
#     for i in range(10**8):
#         total += i
#     print("Done!")
#
#
# if __name__ == "__main__":
#     start = time.time()
#     processes = [Process(target=cpu_heavy) for _ in range(2)]
#
#     # Start both processes
#     [p.start() for p in processes]
#
#     # Wait for both to finish
#     [p.join() for p in processes]
#
#     end = time.time()
#
#     print(f"Time taken with MULTIPROCESSING: {end - start:.2f} seconds.")


# ------------------------------------
#* Process Queue With Example — Passing Data Between Processes
# ------------------------------------

# from multiprocessing import Queue, Process
#
# # Function to prepare chai and send message into queue
# def prepare_chai(queue):
#     queue.put("Masala chai is ready! ☕")
#
#
# if __name__ == "__main__":
#     queue = Queue()
#
#     # Create a process and pass queue as argument
#     p = Process(target=prepare_chai, args=(queue,))
#
#     p.start()
#     p.join()
#
#     # Retrieve message from queue
#     print(queue.get())


# ------------------------------------
#* Process Value With Example — Shared Memory Between Processes
# ------------------------------------

from multiprocessing import Process, Value


# Shared counter increment function
def increment(counter):
    for _ in range(100000):
        # Lock ensures thread-safe (process-safe) increments
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    # Shared integer ('i' = int type, initial value = 0)
    counter = Value("i", 0)

    # Create 4 processes, all incrementing the same shared counter
    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]

    # Start all
    [p.start() for p in processes]

    # Wait for all to complete
    [p.join() for p in processes]

    print(f"✅ Final counter value: {counter.value}")


# ------------------------------------
# Summary:
# - Threads share memory → blocked by GIL → not ideal for CPU-heavy
# - Processes = true parallel execution → faster for number crunching
# - Queue → allows communication between processes
# - Value → allows sharing variables safely
# TODO: TIP - Uncomment each section one by one to try
# ------------------------------------
