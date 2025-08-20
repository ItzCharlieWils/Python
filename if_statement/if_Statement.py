#if condition:
#    execute if the condition is true / unless, skip
# elif condition: (use 'elif' if there is two or more conditions and can add 'elif' infinitely)
#    execute if the first condition is false
# else:
#    execute if condition is false (or) all the above conditions are false


age = int(input("Enter your age: "))

if age >= 18:
    print("You are Signed")
elif age < 0 :
    print("You haven't been borned yet!!")
elif age >= 100:
    print("You are too old to Signed!!")
else :
    print("You need to be at least 18 years old!!")