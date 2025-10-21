# ------------------------------------
# Parallelism in Python ⚡
# ------------------------------------

"""
? What is Parallelism
Parallelism means performing **multiple tasks at the same exact time** using
**multiple CPU cores**. Each process runs truly in parallel — not just switching
rapidly like threads do.

For example 👇
You are **making chai** ☕ while your **friend is serving it** 🍵.
Both tasks happen independently — you don’t wait for each other unless one depends
on the other’s result.

⚙️ Key Idea:
- Runs on **multiple CPU cores**.
- Uses **separate processes** instead of threads.
- Great for **CPU-bound** tasks (like math, image, or data-heavy work).
- Controlled using the built-in `multiprocessing` module.
"""

from multiprocessing import Process
from time import sleep


# * Function to simulate chai brewing work done by different makers
def brew_chai(name):
    print(f"🔥 Start of {name} brewing")
    sleep(3)  # * Simulate brewing time (each process sleeps independently)
    print(f"✅ End of {name} brewing")


if __name__ == "__main__":
    # * Create multiple processes — each will run in parallel on a different CPU core
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai maker #{i+1}",)) for i in range(3)
    ]

    # * Start all processes → each chai maker starts brewing at the same time
    for p in chai_makers:
        p.start()

    # * Wait for all processes to complete before printing the final message
    for p in chai_makers:
        p.join()

    # * Once all makers finish, print success message
    print("☕ All chai makers finished brewing chai!")

# ? Expected Output Example:
"""
🔥 Start of Chai maker #1 brewing
🔥 Start of Chai maker #2 brewing
🔥 Start of Chai maker #3 brewing
✅ End of Chai maker #1 brewing
✅ End of Chai maker #2 brewing
✅ End of Chai maker #3 brewing
☕ All chai makers finished brewing chai!
"""

# ------------------------------------
# ✅ Summary:
# ------------------------------------
"""
- **Parallelism** → true simultaneous execution on multiple cores.
- **Process()** → creates a separate memory space and runs independently.
- **start()** → begins process execution.
- **join()** → waits for all processes to complete.

! Note: Parallelism is ideal for CPU-heavy tasks,
! while concurrency (threading) is better for I/O-bound tasks.

Todo: Try running both concurrency and parallelism examples side-by-side
Todo: Observe how parallelism completes faster for CPU-intensive work.
"""
