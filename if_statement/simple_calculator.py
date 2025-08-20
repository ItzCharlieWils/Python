num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator: ")


if operator == '+':
    result = num1 + num2 
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2 
    print(f"{num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2 
    print(f"{num1} * {num2} = {result}")
elif operator == '/':
    result = num1 / num2 
    print(f"{num1} / {num2} = {result}")
elif operator == '%':
    result = num1 % num2 
    print(f"{num1} % {num2} = {result}")
elif operator == "**":
    result = num1 ** num2 
    print(f"{num1} ** {num2} = {result}")
elif operator == "//":
    result = num1 // num2 
    print(f"{num1} // {num2} = {result}")
else :
    print("Something went wrong:" \
    "operator should be only '+','-','*','/','%','**','//'")