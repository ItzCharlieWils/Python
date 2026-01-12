import time

my_time = int(input("Enter time in seconds: "))

for x in reversed(range(my_time,0, 3)):
    print(x)
    time.sleep(1)
time.sleep(my_time)


print("Time's up")
