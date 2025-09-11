# ------------------------------------
# Break,Continue Keywords with Loops in Python
# ------------------------------------

"""
? What are break and continue keywords in Python?

* Break
The `break` keyword is used to immediately exit (stop) a loop once a specific condition is met.
In simple words: "Stop the loop right here."

Syntax:
for item in collection:
    if condition:
        break

Example 1:
We have a list of temperature readings of boiling water inside a kettle.
We want to stop checking once the temperature reaches or exceeds 40°C.

temp = [13, 39, 40]
for t in temp:
    if t >= 40:
        print("Temperature limit exceeded at:", t)
        break

# Output:
# Temperature limit exceeded at: 40
"""

"""
* Continue
The `continue` keyword is used to skip the rest of the code in the current iteration
and move on to the next iteration of the loop.

Syntax:
for item in collection:
    if condition:
        continue

Example 2:
We have three ranges of temperature readings:
- Normal → t <= 30
- High   → 30 < t <= 69
- Danger → t >= 70

temp = [10, 20, 30, 40, 50, 70]
for t in temp:
    if 40 <= t <= 69:
        print(f"⚠️ High Temperature: {t}°C, stay alert!")
        continue
    if t >= 70:
        print(f"🚨 Danger! Temperature reached {t}°C")
        break
    print(f"✅ Normal Temperature: {t}°C")

# Output:
# ✅ Normal Temperature: 10°C
# ✅ Normal Temperature: 20°C
# ✅ Normal Temperature: 30°C
# ⚠️ High Temperature: 40°C, stay alert!
# ⚠️ High Temperature: 50°C, stay alert!
# 🚨 Danger! Temperature reached 70°C
"""

# ------------------------------------
#  Real-world Examples
# ------------------------------------

"""
* Example 3: Cart Items Validation (using break)
We want to stop checkout immediately if any item is not available.
"""

cart_items = [
    {"tea": "Masala", "availability": True},
    {"tea": "Ice", "availability": False},
    {"tea": "Lemon", "availability": True},
]

for cart_item in cart_items:
    if not cart_item["availability"]:
        print(f"❌ '{cart_item['tea']}' is not available in stock. Stopping checkout.")
        break
    print(f"✅ {cart_item['tea']} added into your cart")


"""
* Example 4: Tea Menu (using continue)
We want to skip the unavailable tea types and keep serving others.
"""

chai_menu = [
    {"tea": "Masala", "available": True},
    {"tea": "Green", "available": False},
    {"tea": "Lemon", "available": True},
]

for tea in chai_menu:
    if not tea["available"]:
        print(f"⚠️ Skipping {tea['tea']} tea (not available today).")
        continue
    print(f"✅ {tea['tea']} tea is ready to serve!")


"""
📖 Read more from the official Python docs:
https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements
"""
