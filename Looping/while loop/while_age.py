age = int(input("Enter your age: "))
while age <= 0:
    print("Invalid age. Age must be positive.")
    age = int(input("Enter your age: "))
print(f" You are {age} years old.")
