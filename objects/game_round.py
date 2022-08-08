from objects.deck import Deck
from objects.betting_round import BettingRound


class GameRound:
    def __init__(self, round_num, players):
        self.round_num = round_num
        self.dealer = players[-1]
        self.small_blind = players[-2]
        self.big_blind = players[-3]
        self.deck = Deck()
        self.pot = 0
        self.community_cards = []
        BettingRound('pre-flop')
        BettingRound('flop')
        BettingRound('turn')
        BettingRound('river')

    def get_round_num(self):
        return self.round_num

    def get_dealer(self):
        return self.dealer

    def get_small_blind(self):
        return self.small_blind
    
    def get_big_blind(self):
        return self.big_blind
    
    def get_deck(self):
        return self.deck
    
    def get_pot(self):
        return self.pot
    
    def get_community_cards(self):
        return self.community_cards