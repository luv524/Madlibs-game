# the progarm to find languages or something like that. it was a question 6 from the handbook.
friends = {}
for _ in range(4):
    name = input("enter friends name:")
    language = input("enter {friends}'s favourtie language:")
    friends[name] = language
    print(friends)
    