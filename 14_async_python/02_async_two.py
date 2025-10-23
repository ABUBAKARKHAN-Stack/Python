# ------------------------------------
# Async Programming with asyncio.gather()
# ------------------------------------

# * In this example, we'll run multiple async tasks together using asyncio.gather()
# * So all chai types will start brewing at the same time (concurrently)!

import asyncio
import time


# ? Async function: Represents a single chai brewing task
async def brew_chai(name):
    print(f"Brewing {name} chai...")
    await asyncio.sleep(2)  # * Simulates delay (like waiting for water to boil)
    # time.sleep(2)  #! Avoid this in async functions, It blocks the event loop
    print(f"{name} is ready!")


# ? Main async function to handle multiple chai tasks
async def main():
    # * asyncio.gather() runs all async functions concurrently (non-blocking)
    await asyncio.gather(brew_chai("Masala"), brew_chai("Ginger"), brew_chai("Lemon"))


# ? Entry point of async program
asyncio.run(main())

# ------------------------------------
# ✅ Final Summary:
# ------------------------------------
"""
🔑 Key Takeaways:
- `asyncio.gather()` helps run multiple async tasks **together**.
- Each task runs **concurrently** using the event loop.
- Use `await asyncio.sleep()` instead of `time.sleep()` to avoid blocking.
- Ideal for parallel I/O tasks like API calls, downloads, etc.
"""
