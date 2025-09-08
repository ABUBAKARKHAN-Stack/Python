# ------------------------------------
# Lists
# ------------------------------------

"""
? What are Lists in Python?
Lists are collections that can store different types of data such as strings, integers, booleans, etc.
They are mutable datatypes → once created, we can change, add, or remove values.

General Syntax:
    <variable_name> = [value1, value2, value3, ...]

If you are familiar with "Arrays" in other programming languages,
you can think of Lists as a more flexible version of arrays with additional features.
"""

# Definition of a list
ingredients = ["water", "milk", "cardamom", "black tea"]
print(f"Ingredients of tea: {ingredients}")
# Output → Ingredients of tea: ['water', 'milk', 'cardamom', 'black tea']

# ------------------------------------
# Indexing and Accessing
# ------------------------------------
"""
In Python, lists are **zero-indexed**.
This means the index starts from 0 and goes up to (length - 1).

Example:
    ingredients = ["water", "milk", "cardamom", "black tea"]
    Indexes:
    0 → water
    1 → milk
    2 → cardamom
    3 → black tea

print(ingredients[0]) → water
"""

chai_items = ["Masala Tea", "Lemon Tea"]
print(f"{chai_items[0]} is present at 0th index of chai_items list")
# Output → Masala Tea is present at 0th index of chai_items list

# Updating (mutation)
chai_items[0] = "Ice Tea"
print(f"Chai items updated: {chai_items}")
# Output → Chai items updated: ['Ice Tea', 'Lemon Tea']

# ------------------------------------
# List Mutation (Methods)
# ------------------------------------
"""
Lists are mutable → we can perform different operations using built-in methods.
Some common ones are: append(), remove(), pop(), count(), copy(), extend(), insert(), sort(), reverse().
"""

# append()
"""
append(object):
Adds an item at the end of the list.

Example:
    fruits = ["banana", "apple"]
    fruits.append("orange")
    print(fruits) → ['banana', 'apple', 'orange']
"""
ingredients.append("sugar")
print(f"Updated ingredients list: {ingredients}")
# Output → ['water', 'milk', 'cardamom', 'black tea', 'sugar']

# remove()
"""
remove(object):
Removes the first occurrence of the specified item from the list.
It is case-sensitive.

Example:
    fruits = ["banana", "apple"]
    fruits.remove("banana") → ['apple']

Note: If the item does not exist, it will raise a ValueError.
"""
ingredients.remove("water")
print(f"Ingredients after removal of water: {ingredients}")
# Output → ['milk', 'cardamom', 'black tea', 'sugar']

# pop()
"""
pop([index]):
Removes and returns the last element if no index is provided.
If an index is given, removes the item at that index.

Example:
    fruits = ["banana", "apple", "orange"]
    fruits.pop() → removes 'orange'
    fruits.pop(0) → removes 'banana'
"""
popped_item = ingredients.pop()
print(f"{popped_item} is popped from ingredients list")
# Output → sugar is popped from ingredients list

# count()
"""
count(object):
Returns the number of times a specified value occurs in the list.
"""
print(f"Milk present in list: {ingredients.count('milk')} times.")
# Output → Milk present in list: 1 times.

# copy()
"""
copy():
Creates a shallow copy of the list.
Changes made in the copied list do not affect the original list.
"""
ing_copy = ingredients.copy()
print(f"Shallow Copy of ingredients: {ing_copy}")

# extend()
"""
extend(iterable):
Adds elements from another list (or iterable) to the end of the list.

Example:
    fruits = ["apple", "banana"]
    more_fruits = ["orange", "grapes"]
    fruits.extend(more_fruits)
    print(fruits) → ['apple', 'banana', 'orange', 'grapes']
"""
chai_ing = ["water", "milk"]
spices = ["ginger", "cardamom"]
chai_ing.extend(spices)
print(f"Extended Chai Ingredients List: {chai_ing}")

# insert()
"""
insert(index, object):
Inserts an item at a specific position in the list.

Parameters:
- index: The position where the item will be inserted.
- object: The item to insert.

Example:
    fruits = ["apple", "banana"]
    fruits.insert(1, "orange")
    print(fruits) → ['apple', 'orange', 'banana']
"""
ingredients.insert(2, "tea leaves")
print(f"Tea Leaves inserted at 2nd index of ingredients: {ingredients}")
# Output → ['milk', 'cardamom', 'tea leaves', 'black tea']

# sort()
"""
sort():
Sorts the list in ascending order by default.
Can take an optional parameter `reverse=True` for descending order.

Example:
    nums = [3, 1, 2]
    nums.sort()
    print(nums) → [1, 2, 3]
    nums.sort(reverse=True)
    print(nums) → [3, 2, 1]
"""
ingredients.sort()
print(f"Sorted Ingredient list: {ingredients}")

# reverse()
"""
reverse():
Reverses the list in place (does not sort, just flips order).

Example:
    nums = [1, 2, 3]
    nums.reverse()
    print(nums) → [3, 2, 1]
"""
ingredients.reverse()
print(f"Reversed Ingredient list: {ingredients}")

# min() and max()
"""
min(iterable), max(iterable):
These are built-in Python functions (not list methods).
They return the smallest and largest values in a list.

Example:
    nums = [3, 1, 5]
    print(min(nums)) → 1
    print(max(nums)) → 5
"""
sugar_level = [1, 2, 3, 4, 5]
print(f"Maximum Sugar Level: {max(sugar_level)}")
print(f"Minimum Sugar Level: {min(sugar_level)}")


# ------------------------------------
# Summary
# ------------------------------------
"""
✅ Summary:
- Lists are ordered, mutable collections.
- Useful when you need a dynamic set of values that can grow/shrink.
- Support powerful operations like slicing, comprehensions, and nesting.
- Most commonly used Python datatype after strings.
- Slicing works the same way as with strings — try it yourself!

📘 Official Docs: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
"""
