food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You Like: {food}")
    food = input("Enter another food you like (q to quit): ")
print("Thank you for sharing your favorite foods!")