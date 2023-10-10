import random


choices = {0: "Rock", 1: "Paper", 2: "Scissors"}

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)

while user_choice not in [0, 1, 2]:
    user_choice = int(
        input(
            "Wrong value. What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
        )
    )

computer_choice = random.randint(0, 2)

print(
    f"\nYour choice was {choices[user_choice]} and Computer choice was {choices[computer_choice]}.\n"
)
if computer_choice == user_choice:
    print("It's a Draw")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
elif user_choice == 1 and computer_choice == 0:
    print("You Win")
else:
    print("You Lose")
