def is_valid(password):
    if len(password) < 8:
        return False

    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
            break


    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    return has_uppercase and has_digit

while True:
    password = input("Create a password (at least 8 characters, 1 uppercase letter, 1 number): ")

    if is_valid(password):
        print("Password created successfully!")
        break
    else:
        print("Password does not meet requirements. Please try again.")
