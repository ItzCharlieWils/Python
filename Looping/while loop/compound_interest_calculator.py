principle = 0 
rate = 0
time = 0 

while True:
    principle = float(input("Enter the principal amount: "))
    if principle < 0:
        print("Invalid input. Principal must be positive.")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate <0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time <0:
        print("Time can't be less than zero")
    else:
        break


total = principle * (1 + rate / 100) ** time
print(f"The total amount after {time} years is: ${total:.2f}")  