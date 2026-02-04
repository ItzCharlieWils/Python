a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, %, modulus, **, //): ")

def adding(a, b):
    return a + b
def subtracting(a, b):
    return a - b
def multiplying(a, b):
    return a * b    
def dividing(a, b):
    return a / b
def modulus(a, b):
    return a % b
def exponent(a, b):
    return a ** b
def floor_dividing(a, b):
    return a // b
def calculator(a, b, operation):
    if operation == '+':
        return adding(a, b)
    elif operation == '-':
        return subtracting(a, b)
    elif operation == '*':
        return multiplying(a, b)
    elif operation == '/':
        return dividing(a, b)
    elif operation == '%':
        return modulus(a, b)
    elif operation == '**':
        return exponent(a, b)
    elif operation == '//':
        return floor_dividing(a, b)
    else:
        return "Invalid operation"
result = calculator(a, b, operation)
print("The result is:", result)

