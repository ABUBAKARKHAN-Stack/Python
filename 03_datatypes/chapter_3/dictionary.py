# ------------------------------------
# Dictionary
# ------------------------------------

"""
? What are Dictionaries in Python?
Dictionaries are a built-in mutable data type in Python used to store data in **key-value pairs**.

General Syntax:
    <variable_name> = dict(key1=value1, key2=value2, ...)
                      OR
    <variable_name> = {
        "key1": value1,
        "key2": value2,
        ...
    }

💡 If you are familiar with **objects** in JavaScript,
Python dictionaries are very similar (with a slightly different syntax).
"""

# Definition

# Via dict() function
chai_order = dict(type="Ice Tea", size="Small", sugar="2-ts")
print(f"Chai Order: {chai_order}")
# Output → {'type': 'Ice Tea', 'size': 'Small', 'sugar': '2-ts'}

# Via general method
chai_order2 = {"type": "Lemon", "size": "Large", "sugar": "2-ts"}
print(f"Chai Order2: {chai_order2}")
# Output → {'type': 'Lemon', 'size': 'Large', 'sugar': '2-ts'}

# ------------------------------------
# Adding, Accessing, Deleting
# ------------------------------------

chai_recipe = {}  # Start with an empty dictionary

# Adding values
"""
To add a new key-value pair:
    dict_name["key"] = value

Example:
    user = {}
    user["name"] = "Abubakar"
"""
chai_recipe["base"] = "Black Tea"
chai_recipe["liquid"] = "Milk"
print(f"Recipe of chai: {chai_recipe}")
# Output → {'base': 'Black Tea', 'liquid': 'Milk'}

# Accessing values
"""
Access by key:
    dict_name["key"] → returns value
⚠️ Raises KeyError if the key does not exist.

Safe way:
    dict_name.get("key", <default_value>)
Returns the value if key exists, otherwise returns <default_value>.
"""
print(chai_recipe["base"])  # Black Tea
print(chai_recipe.get("liquid"))  # Milk
print(chai_recipe.get("strength", "No Strength Exists"))  # Safe access

# Deleting values
"""
To delete a key-value pair:
    del dict_name["key"]

Example:
    del user["age"]
"""
del chai_recipe["liquid"]
print(f"Chai Recipe after deletion: {chai_recipe}")
# Output → {'base': 'Black Tea'}

# Membership Testing
"""
We can check if a key exists in a dictionary using the 'in' keyword.

Example:
    "name" in user → True if key exists
"""
print(f"Is 'base' property present? {'base' in chai_recipe}")

# ------------------------------------
# Dictionary Methods
# ------------------------------------

chai_order = dict(type="Ice Tea", size="Large", sugar="2-ts")

# keys()
"""
keys():
Returns a view object containing all the keys of the dictionary.
"""
print(f"Chai Order Keys: {chai_order.keys()}")

# values()
"""
values():
Returns a view object containing all the values of the dictionary.
"""
print(f"Chai Order Values: {chai_order.values()}")

# items()
"""
items():
Returns a view object with all key-value pairs as tuples.
"""
print(f"Chai Order Items: {chai_order.items()}")

# pop()
"""
pop(key):
Removes the specified key and returns its value.
⚠️ Raises KeyError if the key does not exist.
"""
removed_type = chai_order.pop("type")
print(f"Removed Type: {removed_type}")
# Output → Removed Type: Ice Tea

# popitem()
"""
popitem():
Removes and returns the last inserted key-value pair as a tuple.
"""
last_item = chai_order.popitem()
print(f"Removed last property: {last_item}")

# update()
"""
update(dict):
Updates the dictionary with key-value pairs from another dictionary.
If the key already exists, its value will be updated.
"""
extra_spices = {"cardamom": "crushed"}
chai_recipe.update(extra_spices)
print(f"Updated Chai Recipe Dict: {chai_recipe}")

# ------------------------------------
# Note
# ------------------------------------
"""
✅ Summary:
- Dictionaries store data in key-value pairs.
- Keys must be unique and immutable (strings, numbers, tuples).
- Values can be any data type (string, list, dict, etc.).
- Very powerful and widely used in Python for structured data.

📘 Official Documentation:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
"""