# ------------------------------------
# Mini Project 4: Tea Stall Billing System
# ------------------------------------

"""
📌 Concept:
We are building a simple billing system for a tea stall.  
We have two separate lists: one containing customer names and another containing their bill amounts.  
Our task is to combine these lists and display each customer's name along with their bill.  

Normally, managing two parallel lists can be tricky.  
To solve this, Python provides the built-in `zip()` function.

? What is zip()?
- The zip() function combines two or more iterables (like lists, tuples, etc.) into pairs (tuples).
- It returns an **iterator of tuples** (not a list by default).
- Syntax: zip(iterable1, iterable2, ...)

General Syntax with for-loop:
for item1, item2 in zip(list1, list2):
    # code using item1 and item2
"""


# Two lists → names of customers and their bills
names = ["Abubakar", "Jhon", "Mira", "Sam"]
bills = [20, 31, 455, 32]

# Loop with zip() to combine names and bills
for name, bill in zip(names, bills):
    print(f"{name} has a bill of Rs {bill}")


"""
📝 Explanation:
- We created two lists: one for customer names and one for their bills.  
- Using zip(names, bills), Python combined both lists into pairs like: ("Abubakar", 20), ("Jhon", 31), etc.  
- The loop then printed each pair in a readable format.  

👉 Key Point:
- zip() by default returns a **zip object** (an iterator).  
- This means it doesn’t immediately create a list, which saves memory.  
- If we want a list of pairs, we can explicitly convert it:
    list(zip(names, bills))  
    → [('Abubakar', 20), ('Jhon', 31), ('Mira', 455), ('Sam', 32)]

⚡ Extra Tip:
- If the lists have different lengths, zip() stops at the shortest list.  
- Example:
    names = ["A", "B"]
    bills = [10, 20, 30]
    for n, b in zip(names, bills):
        print(n, b)   # Only pairs "A-10" and "B-20"
"""