name = input("Enter your Name: ")
print("Welcome "+name+" to the adventure game!! ")

print("You are on a road and its has come to an end. You can go left or right: ")
answer = input("Left or Right: ").lower()

if answer == "left":
    answer = input("You come to a river. You can swim across the river or you can walk around... walk/swim: ").lower()
    if answer == "swim":
        print("You got attacked by aligator. You lost ")
    elif answer == "walk":
        print("You ran out of fuel and you lost")
    else:
        print("Invalid input")
elif answer == "right":
    answer = input("You came to a bridge and its look not safety. What do you do? back/cross: ").lower()
    if answer == "cross":
        print("You back into main road and you won")
    elif answer == "back":
        print("You walked many more miles back and you cant find your way. You lose: ")
    else:
        print("Invalid input")
else:
    print("Invalid input")
