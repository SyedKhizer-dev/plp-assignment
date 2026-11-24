user_name = input("Enter your name: ")
print(f"type of user_name is {type(user_name)}\n")

user_age = input("Enter your age: ")
print(f"type of user_age is {type(user_age)}\n")

# (a)
user_age = int(user_age)
print(f"type of user_age is {type(user_age)}")
print(f"{user_name} was born on {2025-user_age}\n")

# (b)
if user_age % 2 == 0:
    print("Age is even")
else:
    print("Age is odd")

# (c)
user_age = float(user_age)
print(f"\ntype of user_age is {type(user_age)}")
result = user_age / 80
print(f"Formatted result: {result:.4f}\n")

# (e)
# str 30 3.75 False 