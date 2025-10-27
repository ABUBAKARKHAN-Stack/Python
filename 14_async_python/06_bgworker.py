# ------------------------------------
# 🧵 Running Threads Alongside AsyncIO
# ------------------------------------
# * In this example, we’ll mix a background thread with an async event loop.
# * The thread runs continuously (logging system health),
#   while the async coroutine performs a separate task (fetching an order).

import asyncio
import threading
import time


# ? Regular (blocking) function — runs forever in a separate background thread
def background_worker():
    while True:
        time.sleep(1)  # * Blocking sleep is fine here since it’s running in a thread
        print("🩺 Logging the system health...")


# ? Async function — simulates a short async task
async def fetch_order():
    print("🛒 Fetching order from database...")
    await asyncio.sleep(3)  # * Non-blocking async sleep
    print("✅ Order fetched!")


# * Start the background thread
# * daemon=True → thread will automatically stop when the main program exits
threading.Thread(target=background_worker, daemon=True).start()

# * Run the async function (event loop)
asyncio.run(fetch_order())


# ------------------------------------
# ✅ Final Summary:
# ------------------------------------
"""
🔑 Key Takeaways:
- Threads and asyncio can run **side by side**.
- Use threads for continuous or blocking background tasks (like monitoring, logging, etc.).
- AsyncIO handles short I/O-bound tasks efficiently without blocking.
- `daemon=True` ensures background threads exit automatically when main thread ends.
- Perfect pattern when you need a lightweight
"""