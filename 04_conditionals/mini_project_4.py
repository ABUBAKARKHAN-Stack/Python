# ------------------------------------
# Mini Project 4: Smart Thermostat Alert System
# ------------------------------------

"""
📌 Concept:
In this project, we’re simulating a **smart thermostat system**.
It should:
    1. First check if the device is active (status = "active").
    2. If active, check the device temperature.
    3. Trigger alerts if the temperature goes beyond a safe limit.

⚡ Why Nested If?
- Sometimes we need to perform a check only when another condition is true.
- Example: Temperature should only be checked if the device is ACTIVE.
- That’s where **nested if** statements come in.

🛠 Scenario:
- If device is "active":
    - If temperature > 35 → High temperature alert.
    - Else → Normal temperature.
- If device is NOT "active":
    - Show device is offline.
"""

# Step 1: Device status & temperature
device_status = "active"
device_temp = 40

# Step 2: Nested conditions
if device_status == "active":
    if device_temp > 35:
        print("🚨 High Temperature Alert!")
    else:
        print("✅ Temperature is normal.")
else:
    print("⚠️ Device is offline.")

"""
📝 Explanation:
- First IF checks device_status.
- Inside it, another IF checks the temperature.
- This nesting ensures we only care about temperature **when the device is active**.
- ELSE at the outer level handles offline status.

👉 This project is your first step into **nested conditionals**,
a common pattern in IoT devices, smart systems, and real-time monitoring.
"""