import random
from objects.card import Card


class Deck:
    def __init__(self):
        self.deck = [Card(value, suit) for value in range(1, 14) for suit in ['C', 'D', 'H', 'S']]
        random.shuffle(self.deck)

    def get_deck(self):
        return self.deck