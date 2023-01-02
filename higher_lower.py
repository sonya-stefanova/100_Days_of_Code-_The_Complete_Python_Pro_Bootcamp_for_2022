from game_data_higher_lower import data
import random
from art_higher_lower import logo, vs

def random_infleuncer_choice(data):
    choice = random.choice(data)
    return choice #returns dictionary element from the list

def format_result(comparative_item):
    return f"{comparative_item['name']}, a {comparative_item['description']}, from {comparative_item['country']}"


def follower_count(first_compare_followers, second_compare_followers, answer):
    if first_compare_followers>second_compare_followers:
        answer = "a"
    else:
        answer = "b"
    print(answer)
    return answer


def game_play():
    scores = 0
    game_over = False
    first_compare = random_infleuncer_choice(data)

    while not game_over:
        """generate the 2 comparable items"""
        second_compare = random_infleuncer_choice(data)

        """print the comperable items"""
        print(f"Compare A |==> {format_result(first_compare)}")
        print(vs)
        print(f'Compare B |==> {format_result(second_compare)}')

        """print who wins"""
        first_compare_followers = first_compare["follower_count"]
        second_compare_followers = second_compare["follower_count"]
        answer = ""
        answer = follower_count(first_compare_followers, second_compare_followers, answer)

        user_guess = input("Guess who has more followers. Type 'a' or 'b': ")

        if user_guess == answer:
            scores+=1

            print(f"└║ ՞ ౪ ՞ ║┘Hurrey! You guessed the answer: {answer} and your scores are: {scores}!")
        else:
            game_over = True
            print(f"Sorry, you lose (◕⌓◕;) Your achievement is: {scores}!")

            restart = True
            while restart:
                ask_for_restart = input("Do you want to proceed playing? Type 'Y' or 'N': ").lower()
                if ask_for_restart == "yes" or ask_for_restart == "y":
                    game_play()
                elif ask_for_restart == "n" or ask_for_restart == "no":
                    print(f"Thanks for being here! GOOD BYE!")
                    restart = False
                else:
                    print(f"Thanks for being here! GOOD BYE!")
                    restart = False
    first_compare = second_compare
game_play()