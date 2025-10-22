# ------------------------------------
# More on Threads
# ------------------------------------


import threading

# ------------------------------------
# 🧵 Threading Example — Downloading Images Concurrently
# ------------------------------------

# import requests
# import time

#* Function to simulate downloading images from the internet
# def download_image(url):
#     print(f"Start download from {url} image...")
#     resp = requests.get(url)
#     print(f"Finished downloading from {url} size {len(resp.content)} bytes")

#* Multiple image URLs to download concurrently
# urls = [
#     "https://plus.unsplash.com/premium_photo-1760705088738-32f7a991dba7?w=200",
#     "https://plus.unsplash.com/premium_photo-1760705088738-32f7a991dba7?w=2000",
# ]

# start = time.time()  #* Record start time to measure performance

# threads = []  #* List to store thread objects

# //* Create and start a thread for each image download
# for url in urls:
#     t = threading.Thread(target=download_image, args=(url,))
#     t.start()
#     threads.append(t)

# //* Wait for all threads to complete before moving on
# for t in threads:
#     t.join()

# end = time.time()  #* Record end time

# print(f"All downloads done in {end - start:.2f} seconds")

#? Above code demonstrates I/O-bound concurrency using threads.
#? Even though Python has a GIL (Global Interpreter Lock),
#? threads are useful for tasks waiting on I/O (like downloading files or APIs).


# ------------------------------------
# 🧮 Thread Synchronization — Using Lock
# ------------------------------------

counter = 0  #* Shared resource (global variable)
lock = threading.Lock()  #* Lock to prevent race conditions


#* Function to increment a shared counter safely
def increment():
    global counter
    for _ in range(1000000):
        #* Acquire the lock before modifying the shared variable
        with lock:
            counter += 1  #* Only one thread can update this at a time


#* Create 10 threads that all increment the same counter
threads = [threading.Thread(target=increment) for _ in range(10)]

#* Start all threads concurrently
[t.start() for t in threads]

#* Wait for all threads to finish before printing the result
[t.join() for t in threads]

#* Print the final result after all threads complete safely
print(f"Final Counter {counter}")

# ------------------------------------
# ✅ Explanation
# ------------------------------------
#* Without the Lock:
#   - Multiple threads may try to modify `counter` simultaneously.
#   - This causes a **race condition**, leading to incorrect results.
#
#* With the Lock:
#   - Only one thread updates `counter` at a time.
#   - Prevents data corruption and ensures correct count.

#? This example focuses on CPU-bound code (incrementing numbers),
#? where threading doesn’t offer real speed-up due to GIL,
#? but demonstrates how to handle shared data safely.

# ------------------------------------
# ✅ Summary:
# ------------------------------------
# - **threading.Lock()** → prevents multiple threads from accessing shared data at once.
# - **with lock:** → ensures atomic operations on shared resources.
# - **join()** → waits for all threads to finish.
# - Threading works best for **I/O-bound tasks**, not **CPU-bound tasks**.

#Todo Try removing the lock and see how the final counter becomes inconsistent.