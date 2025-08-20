unit = input("Enter a unit for temperature(F or C): ")
temperature = float(input("Enter temperature value: "))

if unit =='C':
    temperature = (temperature*9/5) + 32
    print(f"Converted temperature from Celsius to {round(temperature, 1)} F")
elif unit == 'F':
    temperature = (temperature - 32)* 5/9
    print(f"Converted temperature from Fahrenheit to {round(temperature, 1)} C")
else:
    print(f"invalid {unit}, it should be only F or K")