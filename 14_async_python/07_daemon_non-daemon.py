# ------------------------------------
# Daemon VS Non-Daemon Thread
# ------------------------------------
"""
? Daemon Thread:
A Daemon thread is a background thread that automatically terminates 
when the main thread (or program) finishes execution. 
It’s mainly used for background tasks like monitoring or logging that don’t need 
to prevent the program from exiting.

? Non-Daemon Thread:
A Non-Daemon thread (default type) keeps running even after the main thread ends. 
The program will wait for these threads to complete before shutting down. 
They are used when the task must finish before the program exits.
"""

import threading
import time


# ? Background task — simulates monitoring chai temperature
def monitor_chai_temp():
    while True:
        print("🌡️ Monitoring tea temperature...")
        time.sleep(2)  # * Simulate delay between checks


# ------------------------------------
# ☕ Daemon vs Non-Daemon Example
# ------------------------------------

#! Non-Daemon Thread Example:
# tea = threading.Thread(target=monitor_chai_temp)
# * If used, this thread will keep running even after main program ends.

# ✅ Daemon Thread Example:
tea = threading.Thread(target=monitor_chai_temp, daemon=True)
# * Daemon threads automatically terminate when the main program finishes.
tea.start()

print("✅ Main program done!")


# ------------------------------------
# ✅ Final Summary:
# ------------------------------------
"""
🔑 Key Takeaways:
- **Daemon Thread** → Runs in background and stops automatically when main thread exits.
- **Non-Daemon Thread** → Keeps running even after main thread ends (program waits for it).
- Use Daemon threads for background monitoring, logging, or lightweight tasks.
- Check type using `thread.daemon` → True = Daemon, False = Non-Daemon.
"""
