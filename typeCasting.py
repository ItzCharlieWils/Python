#Type Casting = the process of converting one data type to another
#       str(), int(), float(), bool()

name = "Charlie"
age = 20
gpa = 3.4
is_student = True
print("Before Type Casting \n")
print("name", type(name),"\n" ,"age",type(age),"\n","gpa",type(gpa),"\n", "is_student",type(is_student))

name = bool(name)
age = float(age)
gpa = str(gpa)
is_student = int(is_student)

print("After type casting \n")
print("name", type(name),"\n" ,"age",type(age),"\n","gpa",type(gpa),"\n", "is_student",type(is_student))
print(f"name {name} \n age {age} \n gpa {gpa} \n is_student {is_student}")