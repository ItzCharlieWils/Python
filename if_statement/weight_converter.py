weight = float(input("Enter your weight: "))
unit = input("Enter weight input unit (K or L): ")

if unit =="K":
    weight = weight * 2.05
    unit ="Lb"
    print("converted to Lb")
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit =="L":
    weight = weight / 2.05
    unit ="Kg"
    print("converted to kg")
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid")