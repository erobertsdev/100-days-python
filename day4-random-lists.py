import random
import my_module # module with pi variable

# random.seed(1233)

# random_integer = random.randint(1, 10) # random number between 1 and 10 inclusive
# print(random_integer)

# print(my_module.pi)

# random_float = random.random() * 5
# print(random_float)

# heads or tails exercise
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# coin_toss = random.randint(0,1)
# if coin_toss == 0:
#     print("Heads")
# else:
#     print("Tails")

# lists

# states = ["Delaware", "Pennsylvania", "New Mexico", "Colorado"]
# print(states[0]) # Delaware
# states[1] = "Not Pennsylvania"
# print(states)
# states.append('Utah')
# print(states)

# Who pays the bill exercise
# names_list = ['John','Bill','Jennifer','Becky','Todd']
# list_length = len(names_list)
# picker = random.randint(0,list_length - 1)
# print(f"{names_list[picker]} is paying the bill today!")

# Day 4 Project - Rock, Paper, Scissors
plays = ['Rock', 'Paper', 'Scissors']
player_choice = plays[int(input("What's your play? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))]
computer_choice = plays[random.randint(0,2)]
if player_choice == 'Rock':
    if computer_choice == 'Rock':
        print(f"Computer chose {computer_choice} also. TIE GAME!")
    elif computer_choice == 'Paper':
        print(f"Computer chose {computer_choice} which beats {player_choice}. YOU LOSE!")
    else:
        print(f"Computer chose {computer_choice}. {player_choice} beats {computer_choice}. YOU WIN!")
if player_choice == 'Paper':
    if computer_choice == 'Paper':
        print(f"Computer chose {computer_choice}. TIE GAME!")
    elif computer_choice == 'Scissors':
        print(f"Computer chose {computer_choice} which beats {player_choice}. YOU LOSE!")
    else:
        print(f"Computer chose {computer_choice}. {player_choice} beats {computer_choice}. YOU WIN!")
if player_choice == 'Scissors':
    if computer_choice == 'Scissors':
        print(f"Computer chose {computer_choice} also. TIE GAME!")
    elif computer_choice == 'Rock':
        print(f"Computer chose {computer_choice} which beats {player_choice}. YOU LOSE!")
    else:
        print(f"Computer chose {computer_choice}. {player_choice} beats {computer_choice}. YOU WIN!")
