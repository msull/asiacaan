import random
from textwrap import dedent

aronson_stack = {
    'Jack of Spades': 1,
    'King of Clubs': 2,
    '5 of Clubs': 3,
    '2 of Hearts': 4,
    '9 of Spades': 5,
    'Ace of Spades': 6,
    '3 of Hearts': 7,
    '6 of Clubs': 8,
    '8 of Diamonds': 9,
    'Ace of Clubs': 10,
    '10 of Spades': 11,
    '5 of Hearts': 12,
    '2 of Diamonds': 13,
    'King of Diamonds': 14,
    '7 of Diamonds': 15,
    '8 of Clubs': 16,
    '3 of Spades': 17,
    'Ace of Diamonds': 18,
    '7 of Spades': 19,
    '5 of Spades': 20,
    'Queen of Diamonds': 21,
    'Ace of Hearts': 22,
    '8 of Spades': 23,
    '3 of Diamonds': 24,
    '7 of Hearts': 25,
    'Queen of Hearts': 26,
    '5 of Diamonds': 27,
    '7 of Clubs': 28,
    '4 of Hearts': 29,
    'King of Hearts': 30,
    '4 of Diamonds': 31,
    '10 of Diamonds': 32,
    'Jack of Clubs': 33,
    'Jack of Hearts': 34,
    '10 of Clubs': 35,
    'Jack of Diamonds': 36,
    '4 of Spades': 37,
    '10 of Hearts': 38,
    '6 of Hearts': 39,
    '3 of Clubs': 40,
    '2 of Spades': 41,
    '9 of Hearts': 42,
    'King of Spades': 43,
    '6 of Spades': 44,
    '4 of Clubs': 45,
    '8 of Hearts': 46,
    '9 of Clubs': 47,
    'Queen of Spades': 48,
    '6 of Diamonds': 49,
    'Queen of Clubs': 50,
    '2 of Clubs': 51,
    '9 of Diamonds': 52,
}


def main():
    while True:
        try:
            card_choice = random.choice(list(aronson_stack.keys()))
            selected_position = random.choice(list(aronson_stack.values()))
            cut_card = None

            cut_card_index = None

            if aronson_stack[card_choice] == selected_position:
                cut_card = 'None. Miracle!'
            elif aronson_stack[card_choice] < selected_position:
                cut_card_index = 52 + aronson_stack[card_choice] - selected_position
            else:
                cut_card_index = aronson_stack[card_choice] - selected_position
            if cut_card_index is not None:
                for card, value in aronson_stack.items():
                    if cut_card_index == value:
                        cut_card = card
            print(dedent("""
            Selected card is {} at position {}.

            Cut card is....\
            """.format(
                card_choice,
                selected_position,
            )))
            input()
            print(cut_card)
        except KeyboardInterrupt:
            break

