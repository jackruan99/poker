import sys
import os
ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)

from itertools import combinations
from objects.deck import Deck
from objects.hand import Hand


def main():
    deck = Deck()
    combs = combinations(deck.get_deck(), 2)
    all_possible_hands = [Hand(hand) for hand in list(combs)]
    for hand in all_possible_hands:
        print(hand)

if __name__ == "__main__":
    main()


