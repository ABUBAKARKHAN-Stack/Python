# ------------------------------------
# 🌐 Async Programming with aiohttp + asyncio.gather()
# ------------------------------------
# * In this example, we'll fetch multiple URLs concurrently using aiohttp.
# * Thanks to asyncio.gather(), all requests start together (non-blocking & concurrent).

import asyncio
import aiohttp


# ? Async function: Represents a single HTTP fetch task
async def fetch_url(session, url):
    print(f"Fetching: {url} ...")
    async with session.get(url) as response:
        # * Await ensures we don't block the event loop while waiting for the response
        print(f"✅ Fetched {url} with status: {response.status}")


# ? Main async function to manage multiple fetch tasks
async def main():
    # * Example list of URLs (same one repeated thrice for demo)
    urls = ["https://httpbin.org/delay/2"] * 3

    # * aiohttp.ClientSession() is like opening a reusable browser session
    async with aiohttp.ClientSession() as session:
        # * Create async tasks for each URL (but don’t run them yet)
        tasks = [fetch_url(session, url) for url in urls]

        # * asyncio.gather() runs all fetch tasks concurrently 🚀
        await asyncio.gather(*tasks)


# ? Entry point of the async program
asyncio.run(main())

# ------------------------------------
# ✅ Final Summary:
# ------------------------------------
"""
🔑 Key Takeaways:
- `aiohttp` allows asynchronous HTTP requests (non-blocking network I/O).
- `asyncio.gather()` runs all async tasks together (great for concurrent API calls).
- Use `await` when performing network or I/O tasks to avoid blocking the event loop.
- Perfect for fetching multiple URLs, API data, or scraping websites efficiently.
"""