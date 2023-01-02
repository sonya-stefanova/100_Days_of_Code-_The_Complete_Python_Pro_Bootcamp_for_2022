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

options = [rock, paper, scissors]

your_choice = int(input("What is your choice? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if your_choice >= 3 or your_choice < 0:
  print("You type an invalid number!")
  exit()
else:
  print(options[your_choice])

random_choice = random.randint(0, 2)
print("Computer chose:")
print(options[random_choice])


if your_choice == 0 and random_choice == 2:
  print("You win!")
elif random_choice == 0 and your_choice == 2:
  print("You lose")
elif random_choice > your_choice:
  print("You lose")
elif your_choice > random_choice:
  print("You win!")
elif random_choice == your_choice:
  print("Hah, You and the computer think the same way. It's a draw!")