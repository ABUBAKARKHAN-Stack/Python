# ------------------------------------
# Mini Project 3: Tea Menu Printer
# ------------------------------------

"""
📌 Concept:
We are building a program for a café that displays the tea menu with
numbers (like an ordered menu card).

Normally, lists in Python start with index 0,
but for user-friendly menus, we usually want numbering from 1.
For this, Python provides a very handy function called `enumerate()`.

? What is enumerate()?
- The enumerate() function adds a counter to an iterable (like a list, tuple, or dictionary).
- It returns both the index and the value at the same time.
- Syntax: enumerate(iterable, start=0)
  - iterable → list, dict, tuple, etc.
  - start → the starting number of the counter (default = 0)

General Syntax with for-loop:
for index, value in enumerate(iterable, start=1):
    # code to execute with index and value
"""


# Tea menu list
menu = ["Masala Tea", "Ice Tea", "Lemon Tea", "Black Tea"]

# Loop with enumerate to print menu items with numbering
for idx, item in enumerate(
    menu, start=1
):  # start=1 → numbering starts from 1 instead of 0
    print(f"{idx}: {item}")


 # Order Summary Genrats

order_summary = {
     "Jhon": 140,
     "Alex": 122,
     "George": 324,
     "Andery": 199
}
for name,amount in order_summary.items():
   print(f"{name} paid Rs: {amount}")  

"""
📝 Explanation:
- We created a list 'menu' with tea names.  
- Using enumerate(menu, start=1), we got both the index (starting at 1) and the tea name.  
- For every item, the loop prints a numbered list like "1: Masala Tea".

👉 Key Point:
- enumerate() saves us from writing extra code to track indexes.  
- It is widely used when we want both the index and value of a list (or other iterable).

⚡ Extra Tip:
- enumerate() can also work with tuples, sets, and even dictionaries.  
- Example with dictionary:
    menu = {"Masala": 20, "Ice": 25}
    for idx, (tea, price) in enumerate(menu.items(), start=1):
        print(f"{idx}: {tea} - {price} Rs")

⚡ Note:
This project demonstrates how loops and enumerate() make it easy to number items in a list.  
"""
