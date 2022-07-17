import random

from classes.card import Card


class Deck:
    def __init__(self, num_decks=1):
        self.deck = [Card(rank, suit) for _ in range(num_decks)
                     for rank in range(1, 14) for suit in ['C', 'D', 'H', 'S']]
        self.num_decks = num_decks

    def get_deck(self):
        return self.deck

    def get_deck_len(self):
        return len(self.deck)

    def get_num_decks(self):
        return self.num_decks

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card = self.deck.pop()
        card.flip()
        return card

    def deal_to_player(self, player):
        card = self.deck.pop()
        card.flip()
        player.receive_card(card)

    def print_deck(self):
        s = "[ "
        for card in self.deck:
            s += card.get_name() + ' '
        print(s + ']')
