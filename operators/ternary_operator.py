#conditional expression = A one-line shortcut for if-else statement( ternary operator)
#           print or assign one of two values based on a condition
#           X if condition, else Y

num = 4
a = 5
b =  6
age = 16
temperature = 20
user_role = "guest"

print("Positive " if num > 0 else "Negative")
result = "Even" if num% 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "child"
weather = "Hot" if temperature > 25 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(result)
print(max_num)
print(min_num)
print(status)
print(access_level)