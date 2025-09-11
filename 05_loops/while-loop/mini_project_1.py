# ------------------------------------
# Mini Project 1: Tea Temperature Monitor
# ------------------------------------

"""
📌 Concept:
We are creating a simple program to monitor the temperature of tea as it heats up.
The temperature starts at 40°C and increases until it reaches or exceeds 100°C.
This demonstrates how a WHILE loop works.

? What is a WHILE loop?
- A WHILE loop keeps executing a block of code **as long as the condition is True**.
- Once the condition becomes False, the loop stops.

General Syntax:
while condition:
    # code to execute repeatedly
"""

# Initial tea temperature
temp = 40

# WHILE loop to check and display temperature
while temp <= 100:  # loop runs until temp is greater than 100
    print(f"🌡️ Current Temperature of tea: {temp}°C")
    # temp = temp + 15
    temp += 15  # increase temperature by 15 each time

"""
📝 Explanation:
- We initialized 'temp' with 40.
- The WHILE loop checks if temp <= 100.
- On each iteration, it prints the current temperature and increases it by 15.
- Once temp becomes greater than 100, the loop stops.

👉 Key Point:
WHILE loops are useful when the number of iterations is **not fixed in advance**,  
but depends on a condition being True.
"""
