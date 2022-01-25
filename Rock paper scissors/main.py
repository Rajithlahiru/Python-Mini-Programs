import random

user_won = 0
computer_won = 0

options = ["scissors", "paper", "rock"]

while True:
    user_input = input("Enter scissors/ paper/ rock or q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # 0 ==> scissors
    # 1 ==> paper
    # 2 ==> rock

    computer_pick = options[random_number]
    print("Computer picked "+str(computer_pick))

    if computer_pick == "scissors" and user_input == "rock":
        print("you won")
        user_won += 1

    elif computer_pick == "rock" and user_input == "paper":
        print("you won")
        user_won += 1

    elif computer_pick == "paper" and user_input == "scissors":
        print("you won")
        user_won += 1

    elif computer_pick == "paper" and user_input == "paper":
        print("Draw")

    elif computer_pick == "scissors" and user_input == "scissors":
        print("Draw")

    elif computer_pick == "rock" and user_input == "rock":
        print("Draw")

    else:
        print("You lose")
        computer_won += 1

print("You won "+str(user_won)+" times")
print("Computer won "+str(computer_won)+" times")
print("Good bye")
