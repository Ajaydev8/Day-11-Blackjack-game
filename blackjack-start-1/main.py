############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.


from art import logo
import random
# from replit import clear - This code is for replit only



def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().





    # Hint 6: Create a function called calculate_score() that takes a List of cards as input
    # and returns the score.
    # Look up the sum() function to help you do this.

def calculate_score(card_list):
    total = sum(card_list)
    if total == 21:
        return 0
    elif total > 21:
        for card in card_list:
            if card == 11:
                new_card = 1
                card_list.remove(card)
                card_list.append(new_card)
    return total

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        print("You went over. You lose.")
    if user_score == computer_score:
        print("It's a draw")
    elif computer_score == 0:
        print("You lose!, Computer has a Blackjack🤯.")
    elif user_score == 0:
        print("You have a Blackjack😎! You win😎😎😎😎!")
    elif user_score > 21:
        print("You went over😢, You lose.")
    elif computer_score > 21:
        print("Computer went over😁, You win😎😎.")
    elif user_score > computer_score:
        print(f"You win! your total score is {user_score}")
    elif computer_score > user_score:
        print(f"You lose! your score {user_score} is less then computer score {computer_score}")

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of
# the actual score. 0 will represent a blackjack in our game.


# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it
# with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21,
# then the game ends.

    # Continueeeee debuging FROM HEREEEEEEEE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def play_game():

    print(logo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())

    for _ in range(2):
        computer_cards.append(deal_card())

    game_is_on = True

    while game_is_on:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"your cards: {user_cards}, your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_is_on = False
        else:
                # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card()
            #function to add another card to the user_cards List. If no, then the game has ended.

            user_choice = input("Do you want to draw another card? Type 'y' or Type 'n': ").lower()

            if user_choice == 'y':
                user_cards.append(deal_card())
            elif user_choice == 'n':
                game_is_on = False

    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated
    # until the game ends.

    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long
    # as it has a score less than 17.


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f" Your final hand: {user_cards}, your final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


play_game()

    # Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
    # both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses.
    # If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses.
    # If the computer_score is over 21, then the computer loses. If none of the above,
    # then the player with the highest score wins.





    # Hint 14: Ask the user if they want to restart the game. If they answer yes,
    # clear the console and start a new game of blackjack and show the logo from art.py.

# This only work in replit.

# while is_on:
#     blackjack()
#     choice = input("Do you want to play another game of the blackjack? Type 'y' or 'n': ")
#     if choice == 'y':
#         # Warning: clear function will only work in replit
#         clear()
#         blackjack()
#     elif choice == 'n':
#         is_on = False
