from itertools import combinations
from objects.deck import Deck


class Range:
    def __init__(self):
        self.combos = list(combinations(Deck().get_deck(), 2))
    
    def get_range(self):
        return self.combos

    def __str__(self):
        s = "[ "
        for card1, card2 in self.combos:
            s += f'({str(card1)},{str(card2)}) '
        return s + ']'