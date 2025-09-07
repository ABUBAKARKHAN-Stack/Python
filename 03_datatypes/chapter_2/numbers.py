# NUMBERS

"""
? What are numbers in Python?
Numbers are objects (instances of classes) that are used to perform mathematical operations such as 
addition, multiplication, subtraction, division, etc.

* There are different types of numbers in Python:
*** Integers, Floats, Booleans, Complex ***
"""

# Integers
ginger_tea_grams = 5  # Assign 5 (datatype: int) to ginger_tea_grams variable
black_tea_grams = 10  # Assign 10 (datatype: int) to black_tea_grams variable
total_tea_grams = ginger_tea_grams + black_tea_grams  # Basic addition operation
print(f"Total Tea in grams is: {total_tea_grams}")  # Prints 15

remaining_tea_grams = black_tea_grams - ginger_tea_grams  # Subtraction operation
print(f"Remaining Tea in grams is: {remaining_tea_grams}")  # Prints 5

milk_liters = 9  # Assign 9 (datatype: int) to milk_liters variable
servings = 5  # Assign 5 (datatype: int) to servings variable
milk_per_servings = milk_liters / servings  
# Basic division operation. Division always produces a float result, 
# even if both operands are integers. This shows how Python can implicitly
# convert integers into floats.
print(f"Milk Per Serving is: {milk_per_servings}")  # Prints 1.8

total_tea_bags = 9
pots = 5
bags_per_pot = total_tea_bags // pots  
# Floor division: Divides total_tea_bags by pots but discards any fractional part, 
# always returning an integer result.
print(f"Bags per pot is: {bags_per_pot}")  # Prints 1

total_cardmom_pods = 10
pods_per_cup = 3
left_over_pods = total_cardmom_pods % pods_per_cup  
# Modulus operator: Returns the remainder of the division.
print(f"Left Over Pods are: {left_over_pods}")  # Prints 1

num_1 = 10
power_of_num_1 = 3
result = num_1 ** power_of_num_1  
# Exponentiation operator: raises num_1 to the power of power_of_num_1
# Equivalent to 10 * 10 * 10 = 1000
print(f"10 Power 3 is: {result}")  # Prints 1000

total_tea_leaves_harvested = 1_000_000_000  
# Using underscores improves readability for large numbers
print(f"Total Tea Leaves Harvested: {total_tea_leaves_harvested}")  # Prints 1000000000


"""
👉 Official Docs for numbers:
https://docs.python.org/3/library/stdtypes.html#numbers
"""