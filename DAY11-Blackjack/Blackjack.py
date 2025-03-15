# https://games.washingtonpost.com/games/blackjack          -- blackjack game
# https://docs.python.org/3/library/functions.html#sum      -- sum()
# https://developers.google.com/edu/python/lists#list-methods       --List methods

import random

def compare(u_score, c_score):
    if u_score==c_score:
        return "Draw"
    elif c_score == 0:
        return "You Lose, Opponent has blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over, You Lose"
    elif c_score > 21:
        return "Opponent went over, You Win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    user = []
    computer =[]
    end_game = False
    comp_score = -1
    user_score = -1

    def draw_card():
        cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    def calculate_score(card):
        if sum(card) ==21 and len(card) == 2:
            return 0
        if sum(card) > 21 and 11 in card:
            card.remove(11)
            card.append(1)

        return sum(card)
        
    for i in range(2):
        user.append(draw_card())
        computer.append(draw_card())

    while not end_game:
        user_score = calculate_score(user)
        comp_score = calculate_score(computer)
        print(f"Your cards {user}, currrent score {user_score}")
        print(f"Computers first card: {computer[0]}")

        if user_score==0 or comp_score==0 or user_score>21:
            end_game = True
        else:
            a = input("Type 'y' to get another card, 'n' to pass: ")
            if a == "y":
                user.append(draw_card())
            else:
                end_game = True

    while comp_score != 0 and comp_score < 17:
        computer.append(draw_card())
        comp_score = calculate_score(computer)

    print(f"Your final hand {user}, final score: {user_score}")
    print(f"Computer final hand {computer}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()