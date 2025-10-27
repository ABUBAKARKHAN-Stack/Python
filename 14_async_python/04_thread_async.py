# ------------------------------------
# 🧵 Mixing Threads with AsyncIO (run_in_executor)
# ------------------------------------
# * Here, we'll handle a blocking function (time.sleep) safely inside an async program.
# * asyncio itself can't handle blocking I/O — but ThreadPoolExecutor saves the day!

import time
import asyncio
from concurrent.futures import ThreadPoolExecutor


# ? Regular (blocking) function — simulates a slow, CPU-bound or blocking task
def check_stock(item):
    print(f"🛒 Checking {item} in store...")
    time.sleep(3)  # ! BLOCKING OPERATION (would freeze the event loop if run directly)
    return f"{item} stock: 42"


# ? Async function that uses threads for blocking tasks
async def main():
    # * Get current running event loop
    loop = asyncio.get_running_loop()

    # * ThreadPoolExecutor allows blocking functions to run in separate threads
    with ThreadPoolExecutor() as pool:
        # * run_in_executor() runs the blocking task in another thread
        # * It returns an awaitable — so we can still use `await`!
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")

        # * Once thread finishes, we get the result
        print(f"✅ {result}")


# ? Entry point — runs the async event loop
asyncio.run(main())

# ------------------------------------
# ✅ Final Summary:
# ------------------------------------
"""
🔑 Key Takeaways:
- `ThreadPoolExecutor` lets you run blocking functions (like time.sleep or CPU work)
  in background threads, without freezing the async event loop.
- `loop.run_in_executor()` bridges async world 🌍 and threading world 🧵.
- Use this pattern when you need to integrate **blocking I/O** (e.g., file operations, APIs, DB calls)
  inside an **asyncio-based app**.
"""
