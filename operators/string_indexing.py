#accessing elements of as sequence using[] (indexing operator)
#               [start: end: step]

number = "1234-5678-9012-3456"
reverse = number[::-1]  # reversing the string
last_digit = number[-4:]

print(number[0])
print(number[0:4])  # slicing from index 0 to 4
print(number[5:9])  # slicing from index 5 to 9 
print(number[::2])  # slicing with step of 2
print(number[5:])   # slicing from index 5 to the end
print(number[-1])
print(f"XXXX-XXXX-XXXX-{last_digit}")
print(reverse)