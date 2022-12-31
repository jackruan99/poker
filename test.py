import time
from objects.card import Card
from objects.deck import Deck
from objects.range import Range
from analysis.check_hand import check_hand


def test_check_hand():
    # https://en.wikipedia.org/wiki/Poker_probability
    # hand_dict = {9:"straight-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"two-pairs", 2:"one-pair", 1:"high-card"}
    num_hands = 1000000
    counts = [0] * 10
    for _ in range(num_hands//10):
        deck = Deck()
        for _ in range(10):
            hand = [str(deck.deal()) for _ in range(5)]
            counts[check_hand(hand)] += 1
    print([count/num_hands for count in counts])


test_check_hand()
