# # Basic For Loop which prints numbers from 1 to 10

# for i in range(1,10):
#     print(i)

# # Tables from 1 to 10 Using While LOOP

# table = 1
# while table <= 10:
#     value = 1
#     print(f"Table of {table}")
#     while value <= 10:
#        print(f"{table} X {value} = {table * value}")
#        value += 1
#     table += 1


# # Star Pattern Using While LOOP

# lines = 10

# while lines >= 1:
#     star = 1
#     while star <= lines:
#         print(star,end = " ")
#         star += 1
#     lines -= 1
#     print()


# # for in loop using with lists
# fruits_items = ["Banana", "Orange", "Pineapple", "Apple"]

# for fruit in fruits_items:
#     print(fruit)


# # for in loop using with dict
# user = {
#     "name": "Abubakar",
#     "age": 17,
#     "skill-set": ["JS/TS","MERN","DOCKER","PYTHON"]
# }

# for keys in user:
#     print(keys)


# flavors = ["masala", "ice", "lemon"]

# print("All available flavors: ", flavors)
# while True:
#     flavor = input("Choose your flavor: ").lower()
#     if flavor not in flavors:
#         print(f"{flavor} is not available")
#         continue
#     break
# print(f"You choose - {flavor} flavor")

# while (flavor := input("Choose your flavor: ").lower()) not in flavors:
#     print(f"{flavor} is not available")
# print(f"You choose - {flavor} flavor")


# users = [
#     {"id": 1, "total": 100, "cupon": "P10"},
#     {"id": 2, "total": 140, "cupon": "P70"},
#     {"id": 3, "total": 1000, "cupon": "P95"},
#     {"id":4,"total": 1400}
# ]

# discounts = {
#     "P10": (0, 10),
#     "P70": (0.7, 0),
#     "P95": (0.95, 0),
# }

# for user in users:
#     (percent, flat) = discounts.get(user.get("cupon"), (0, 0))
#     discount = user["total"] * percent + flat
#     user["total"] -= discount
#     print(f"User {user["id"]} paid Rs: {user['total']} and get {(str(percent * 100) + "%" ) if percent else (str(flat) + " Rs") } discount")