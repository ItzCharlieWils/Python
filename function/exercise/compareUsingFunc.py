a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def compare(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is less than {b}"
    elif a == b:
         return f"{a} is equal to {b}"
    else:
        return f"{a} is not equal to {b}"
result = compare(a, b)
print(result)

