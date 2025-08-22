#validate user input exercise
#1. username is no more than 12 characters
#2. username must no contain spaces
#3. username must not contain digits

username = input("Enter username: ")

if len(username) > 12  :
    print("Username should be less than 12 characters")
elif not username.find(" ") == -1:
    print("Username should not contain space")
elif not username.isalpha()  :
    print("Username should not contain numbers")
else: 
    print(f"Hello {username}")