import random
from art import logo
#TODO make a function for choise a new card
def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#TODO make a function that calculate score

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

#compare user_score and computer_score

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose,  opponent has Blackjack"
    elif u_score == 0:
        return "win with a blackjack"
    elif u_score > 21:
        return "you went over. you lose"
    elif c_score > 21:
        return "Opponent went over, you win"
    elif u_score > c_score:
        return "you win"
    else:
        return "you lose"

#TODO make a empty list fro user and computer
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    #TODO use a for loop for adding a cards in lists

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #here we give cars now how many cards score they have calculate using function
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")


        #here i make game over condition, in certain condition game is over

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"your final hand: {user_cards}, final score: {user_score}")
    print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))



while input("Do you want to play a game of Blackjack? type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
