import random
from guess_time_art import logo

EASY_TURNS = 10
HARD_TURNS = 5

#generate a secret number
def secret_number_generator():
    secret_number = random.randint(1, 100)
    print(f"Peak at the secret number: {secret_number}")
    return secret_number


#Make function to set a difficulty level.
def difficulty_choice():
  difficulty = input("Choose a difficulty. 'Easy' or 'Hard': ").lower()
  if difficulty == "easy":
      print(f"You choose the easy way ;). You have {EASY_TURNS} turns.")
      return EASY_TURNS
  elif difficulty == "hard":
      print(f"It would be a challenge! You choose the hard way! You start with {HARD_TURNS} turns.")
      return HARD_TURNS
  else:
      type_another_diff = input("Are you sure you've written the correct word? Type EASY OR HARD!")

#Function to check user's guess against actual answer.
def check_answer(guess, secret_answer):
  if guess > secret_answer:
      print("Too high. Try again.")
  elif guess < secret_answer:
      print("Too low. Try again.")
  else:
      print(f"Well done! Your guess is correct. The secret answer is: {secret_answer}.")

def game_play():
    print(logo)
    #Choosing a random number between 1 and 100.
    print("Welcome to the Secret Number Game!")
    print("Opt for a number from 1 and 100.")
    secret_answer = secret_number_generator()
    attempts = difficulty_choice()
    #Repeat the guessing functionality if they get it wrong.

    guess = int(input("Make а guess: "))
    lose = False
    while guess != secret_answer:
        left_turns = check_answer(guess, secret_answer)
        attempts-=1
        print(f"You have {attempts} attempts remaining to guess the number.")
        if attempts <= 0:
            lose = True
            break

        #Let the user guess a number.
        guess = int(input("Make another guess: "))

    if lose:
        print("You've run out of guesses, you lose.")
    else:
        print(f'AWSOME!YOU WIN!')
game_play()
