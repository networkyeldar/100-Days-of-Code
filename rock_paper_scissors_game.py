import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:"))
computer_choice = random.randint(0,2)
if your_choice > 2 or your_choice < 0:
  print("You type invalide number, You Lose!")
else:
  result = (f"Your choice {list[your_choice]} Computer Choice {list[computer_choice]}")
  if your_choice == 0 and computer_choice == 2:
    print(result)
    print("You win!")
  elif your_choice == 0 and computer_choice == 1:
    print(result)
    print("You lose!")
  elif your_choice == 1 and computer_choice == 0:
    print(result)
    print("You win!")
  elif your_choice == 1 and computer_choice == 2:
    print(result)
    print("You lose!")
  elif your_choice == 2 and computer_choice == 0:
    print(result)
    print("You lose!")
  elif your_choice == 2 and computer_choice == 1:
    print(result)
    print("You win!")
  else:
    print(result)
    print(f"Draw!")
