our_list = ["football", "badminton", "golf", "tennis"]
print(our_list)
our_list.append("cricket")
print(our_list)
our_list.remove("golf")
print(our_list)
print(len(our_list))

for sport in our_list:
    print("I like to play", sport)
