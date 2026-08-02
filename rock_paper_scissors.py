
print("TEST - NEW VERSION")

import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5:
    print(f"Score: You {player_score} - Computer {computer_score}")
    player = input("Choose rock, paper or scissors: ")
    print("Choice saved!")
    
    
    if player not in choices:
        print("Invalid choice!")
        continue
    
    computer = random.choice(choices)
    
    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("It's a tie!")
        
    elif player == "rock" and computer == "scissors":
        print("You win!")
        player_score += 1
        
    elif player == "paper" and computer == "rock":
        print("You win!")
        player_score += 1
    
    elif player == "scissors" and computer == "paper":
        print("You win!")
        player_score += 1
    
    else:
        print("Computer wins!")
        computer_score += 1
print(f"Final score: You {player_score} - Computer {computer_score}")

if player_score == 5:
    print("🏆 You won the tournament!")
else:
    print("🤖 Computer won the tournament!")