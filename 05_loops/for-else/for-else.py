# ------------------------------------
# For-Else Loop in Python
# ------------------------------------

"""
📌 Concept:
We are exploring the `for-else` loop in Python.

A `for-else` loop is just like a normal for-loop, but with an **extra `else` block** at the end.  
The `else` block only executes if the loop **completes normally** (without hitting a `break`).  
If the loop exits early due to a `break`, the `else` block will **not execute**.

👉 In simple words:
- If the loop runs fully → `else` executes.
- If the loop is stopped with `break` → `else` does NOT execute.

------------------------------------
✅ General Syntax:
for variable in iterable:
    # loop body
else:
    # executes only if loop wasn't broken
------------------------------------
"""

# Searching for a tea in the menu
chai_menu = ["Masala", "Lemon", "Ice"]

for chai in chai_menu:
    if chai.lower() == "black":
        print(f"✅ {chai} tea found!")
        break
else:
    print("⚠️ Black Tea doesn't exist in the menu.")


# Stock validation
chai_stock = ["Masala", "Green", "Lemon", "Out of stock"]

for tea in chai_stock:
    if tea == "Out of stock":
        print("❌ Stock problem found! Breaking loop.")
        break
    print(f"✅ {tea} is available.")
else:
    print("🎉 All teas are in stock!")


"""
📝 Explanation:
- In Example 1:
  - We searched the menu for "Black Tea".
  - Since it wasn’t found, the loop completed fully, so the `else` block ran.
- In Example 2:
  - The loop broke when "Out of stock" was found.
  - Because of the `break`, the `else` block did not execute.

👉 Key Takeaway:
- Use `for-else` when you want to confirm if a search/iteration completed successfully
  without interruptions (like `break`).

⚡ Real-life Usage:
- Searching for an item in a list (menu, stock, etc.)
- Validation checks (like ensuring everything is available before confirming order)

------------------------------------
🔗 Docs Reference: 
https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
------------------------------------

🎯 Sample Output:
⚠️ Black Tea doesn't exist in the menu.
✅ Masala is available.
✅ Green is available.
✅ Lemon is available.
❌ Stock problem found! Breaking loop.

------------------------------------
💡 Extra Note:
Just like `for-else`, Python also supports a **while-else** loop.  
The behavior is the same: the `else` block runs only if the loop wasn’t interrupted by a `break`.

👉 Try it Yourself:
- Write a `while` loop that searches for a number in a list.
- Use `break` if found, otherwise let the `else` run.
"""
