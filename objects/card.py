class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # 1: ace, ... , 10: 10, 11: jack, 12: queen, 13: king
    def get_value(self):
        return self.value

    # C: clubs, D: diamonds, H: hearts, S: spades
    def get_suit(self):
        return self.suit

    def __str__(self):
        if self.value == 1:
            return 'A' + self.suit
        if self.value == 10:
            return 'T' + self.suit
        if self.value == 11:
            return 'J' + self.suit
        if self.value == 12:
            return 'Q' + self.suit
        if self.value == 13:
            return 'K' + self.suit
        return str(self.value) + self.suit