class Hand:
    def __init__(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def __str__(self):
        return f"{str(self.hand[0]), str(self.hand[1])}"
