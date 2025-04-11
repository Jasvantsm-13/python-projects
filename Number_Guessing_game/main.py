from random import randint
from art import logo
#globle variable
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """ Checks answer against guess, retuns the answer of turns remaining."""
    if user_guess > actual_answer:
        print("too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("too low.")
        return turns - 1
    else:
        print(f"You got it! the answer was {actual_answer}")

# function to set difficulty
def set_difficulty():
    level =  input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print(logo)
    # choosing a random number between 1 to 100.
    print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)

    turns = set_difficulty()
    # track the number of turns and reduce by 1 if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        #let the user guess a number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()

