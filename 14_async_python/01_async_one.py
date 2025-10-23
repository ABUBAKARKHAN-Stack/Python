# ------------------------------------
# Introduction to Asynchronous Programming in Python
# ------------------------------------

"""
? What is Async Programming
Async (asynchronous) programming is used for **I/O-bound tasks** — operations that take time to complete because they rely on external resources, such as:
- Database queries
- API calls
- File reading/writing
- Web requests

It provides **non-blocking execution**, meaning your program doesn’t freeze while waiting for slow I/O operations (like API calls or database queries).  
Instead, Python’s **event loop** switches to other tasks until the awaited one is ready.  

If you’ve ever worked with **JavaScript**, async in Python follows the same concept that gives JS its super-fast, non-blocking behavior.

**EXAMPLE:**
Imagine you’re writing a program that fetches images from the internet and then displays them on a user interface.  
Fetching images is an async (I/O) task. If we use **threading**, it might work — but it will block the main thread until the request either succeeds or fails.  

That’s not ideal because the program “freezes” during the request, and the user can’t see anything happening on the UI.  
Async programming changes the game - it lets you show a loading spinner while the request is being processed, keeping the UI responsive.  
When the request completes, the user either sees the images (on success) or an error message (on failure).  

This is the core benefit of async programming - **smooth, non-blocking, responsive execution**.
"""

# ------------------------------------
# ? How to Do Async Programming in Python
# ------------------------------------

"""
Python provides a built-in library called **asyncio** to work with asynchronous programming.

Every async function declaration starts with the **async** keyword.  
Whenever you need to wait for an I/O task, you use the **await** keyword.  
To execute an async function, you use **asyncio.run()**.

In short:
- `async` → tells Python this function will run asynchronously.
- `await` → pauses just that function until the awaited task completes, allowing other tasks to continue.
- `asyncio.run()` → starts the event loop and runs your async function.

**SYNTAX:**

   import asyncio

   async def <function_name>():
       await <some_io_bound_task>
       # other logic

   asyncio.run(<function_name>())

DEMONSTRATION:
All set! Let’s move to the code part 👇
"""

import asyncio

async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2)  # //* Simulate an I/O delay
    print("Chai is ready!")

asyncio.run(brew_chai())

# ------------------------------------
# ✅ Final Summary:
# ------------------------------------
"""
🔑 **Key Takeaways:**
- **Async Programming** = Runs code on a **non-blocking event loop**, not separate threads.
- Ideal for **I/O-bound tasks** (like API calls, DB queries, web scraping, etc.).
- Uses **async**, **await**, and **asyncio.run()** as core components.
- Keeps your program **responsive** even when waiting for long tasks.
- Avoids blocking the main thread — while one task waits, others keep running.

🧩 **Next Step:**
We’ll explore how to run **multiple async tasks concurrently** using `asyncio.gather()` — to truly see the power of concurrency in action!
"""