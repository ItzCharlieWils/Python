#for loops = execute a block of code repeatedly for a fixed number of times
#           You can iterate over a range, string, sequence, etc.

for x in range(1, 11):  # This will print numbers from 1 to 10
    print(x)
    
for y in range(1, 11, 2):   # This will print numbers from 1 to 10, stepping by 2
    print(y)

for z in reversed(range(1, 11)):  # This will print numbers from 10 to 1
    print(z)
print("Happy new year")

num = "1234-5678-9012-3456"
for x in num:
    print(x)