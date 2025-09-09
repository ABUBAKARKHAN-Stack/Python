# ------------------------------------
# Mini Project 6: Train Seat System
# ------------------------------------

"""
📌 Concept:
This project simulates a train booking system where the user selects 
a seat type, and the program shows details about that seat.

? Why match-case?
- Before Python 3.10, we only had if/elif/else chains.
- With many options, it becomes long and repetitive.
- match-case works like a switch-case in other languages → cleaner, easier to read.

⚡ General Syntax:
    match <expression>:
        case <value1>:
            <code>
        case <value2>:
            <code>
        case _:
            <default_code>   # underscore (_) is like "else"
"""

# Step 1: Ask user to choose seat type
seat_type = input("Please choose seat type (sleeper | ac | general | luxury): ").lower()

# Step 2: Use match-case for clean branching
match seat_type:
    case "sleeper":
        print("Sleeper Class: Beds available, but no AC.")
    case "ac":
        print("AC Class: Comfortable seating with air conditioning.") 
    case "general":
        print("General Class: Basic seating, no AC.")   
    case "luxury":
        print("Luxury Class: AC, beds, and complimentary meals included.")      
    case _:
        print("Invalid seat type. Please choose from sleeper, ac, general, or luxury.")

"""
📝 Explanation:
- The user enters a seat type → program matches it against cases.
- If matched → corresponding details are displayed.
- If no case matches → case _ (default) runs.

👉 This is just a touch into Python’s match-case, 
which makes multiple conditions clean and structured.
"""
