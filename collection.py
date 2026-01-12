#collection = single "variable" used to store multiple values
#example: list, tuple, set, dictionary
#list =[] ordered collection of items (can be changed)
#tuple =() ordered collection of items (cannot be changed)
#set ={} unordered collection of unique items (can be changed)
#dictionary ={} unordered collection of key-value pairs (can be changed)

fruits = ["apple", "orange", "banana", "cherry"]
#print(fruits[2]) 

#for fruit in fruits:
#    print(fruit)

print("apple" in fruits)

fruits.append("kiwi")
fruits.insert(1, "mango")
for fruit in fruits:
    print(fruit)