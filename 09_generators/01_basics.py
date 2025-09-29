# ------------------------------------
# Generators in Python
# ------------------------------------

"""
? What are Generators in Python
Generators are a **special type of function** in Python that return a **stream of values**
instead of generating all values at once.
They are **memory-optimized** and use **lazy evaluation** (values are produced one by one when needed).

👉 Key Points:
- They don’t return the full result immediately.
- They keep track of their state in memory and resume where they left off.
- They always return a **generator object (iterator)**.
- Defined using the special keyword **yield**.

---

? yield Keyword
- `yield` is used inside a generator function instead of `return`.
- Each `yield` pauses the function and gives back a value.
- When called again (via iteration or `next()`), execution resumes from where it stopped.
- This continues until all values are yielded.

---

✅ General Syntax:

    def <function_name>():
        yield <value_1>
        yield <value_2>
        ...

---

? Demonstration:

def get_numbers():
    yield 1
    yield 2
    yield 3

numbers = get_numbers()   # holding reference to generator
print(numbers)            # <generator object ... >

# Iterate over generator
for n in numbers:
    print(n)
# Output:
# 1
# 2
# 3

# Using next()
numbers = get_numbers()
print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers))  # 3
print(next(numbers))  # ❌ Error → StopIteration (all values consumed)
"""

# ------------------------------------
# Example 1: Serving Chai (Iteration)
# ------------------------------------


def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Tea"
    yield "Cup 3: Ice Tea"


stall = serve_chai()

for cup in stall:
    print(cup)

"""
Output:
Cup 1: Masala Chai
Cup 2: Ginger Tea
Cup 3: Ice Tea
"""

# ------------------------------------
# Example 2: Using next() with Generators
# ------------------------------------


def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


chai = get_chai_gen()

print(next(chai))  # Cup 1
print(next(chai))  # Cup 2
print(next(chai))  # Cup 3
# print(next(chai))  # ❌ Uncomment → StopIteration error

# ------------------------------------
# ✅ Final Summary
# ------------------------------------
"""
- Generators are memory-friendly functions that return values one by one.
- They use the `yield` keyword instead of `return`.
- You can loop over them or use `next()` to fetch values step by step.
- They are widely used for handling **large data streams** and **infinite sequences** efficiently.
"""
