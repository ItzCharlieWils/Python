door_is_locked = True
key = int(input("Enter the key number to unlock the door: "))
def unlock_door(door_is_locked, key):
    while door_is_locked:
        if key == 1234:
            door_is_locked = False
            return "Door unlocked!"
        else:
            print("Incorrect key. Try again.")
            key = int(input("Enter the key number to unlock the door: "))
result = unlock_door(door_is_locked, key)
print(result)