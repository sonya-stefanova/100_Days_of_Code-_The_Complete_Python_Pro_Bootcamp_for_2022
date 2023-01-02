from random import randint
from guess_time_art import logo

print(logo)
random_num = randint(1, 101)

print("Welcome to the Number Guessing Game!")
print("Guess a number in the range 1 and 100.")
print(f"Well, the number is: {random_num}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

is_game_over = False

while not is_game_over:
    attempts_remaining = 5
    if difficulty == "easy":
        attempts_remaining = 10

    guessed = False

    guess = int(input("Make a guess: "))
    while not guessed and attempts_remaining != 0:
        print(f"You have {attempts_remaining} attempts to guess the number")
        if guess < random_num:
            print("Too low")
            attempts_remaining -= 1
            guess = int(input("Guess again: "))
        elif guess > random_num:
            print("Too High")
            attempts_remaining -= 1
            guess = int(input("Guess again: "))
        elif guess == random_num:
            print(f"Finally! You hit the answer: {random_num}.")
            guessed = True

    is_game_over = True