import random 

choices = ["rock" , "paper", "scissors"]

player = input("select rock, paper or scissors: ").lower()

computer = random.choice(choices)
print("computer choice: ", computer)

if player == computer:
    print("The match is tied!")

elif player == "paper" and computer == "rock":
        print("You won! paper beats rock")

elif player == "scissors" and computer == "paper":
        print("You won! scissors beats paper")

elif player == "rock" and computer == "scissors":
        print("You won! rock beats scissors")

elif player == "rock" and computer == "paper":
        print("You lost! Try again")

elif player == "paper" and computer == "scissors":
        print("You lost! Try agian")

elif player == "scissors" and computer == "rock":
        print("You lost! Try again")

else:
    print("Invalid Input")
