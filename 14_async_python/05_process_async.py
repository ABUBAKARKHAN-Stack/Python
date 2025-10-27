# ------------------------------------
# ⚙️ Mixing Processes with AsyncIO (run_in_executor + ProcessPoolExecutor)
# ------------------------------------
# * In this example, we’ll combine multiprocessing with asyncio.
# * Useful when you want to run **CPU-bound** tasks (like encryption, image processing)
#   without blocking the async event loop.

import asyncio
from concurrent.futures import ProcessPoolExecutor


# ? CPU-bound function — simulates heavy computation or data encryption
def encrypt(data):
    # * Just a simple reverse operation for demo (pretend it’s real encryption 😅)
    return f"🔒 Encrypted: {data[::-1]}"


# ? Async function that offloads heavy CPU work to another process
async def main():
    # * Get the currently running event loop
    loop = asyncio.get_running_loop()

    # * ProcessPoolExecutor spawns separate **processes**
    #   Ideal for CPU-heavy computations — runs in parallel on multiple cores 🧠
    with ProcessPoolExecutor() as pool:
        # * Run the blocking CPU task in a separate process (non-blocking for event loop)
        result = await loop.run_in_executor(pool, encrypt, "credit_card_1234")

        # * Await ensures async control flow remains smooth
        print(result)


# ? Entry point (required to avoid Windows multiprocessing issues)
if __name__ == "__main__":
    asyncio.run(main())

# ------------------------------------
# ✅ Final Summary:
# ------------------------------------
"""
🔑 Key Takeaways:
- `ProcessPoolExecutor` runs CPU-bound tasks in **separate processes** (true parallelism).
- `ThreadPoolExecutor` is for I/O-bound tasks (network, file, sleep delays).
- `loop.run_in_executor()` can use either — thread or process pools.
- This hybrid model keeps your async app responsive, even during heavy CPU computations.
"""
