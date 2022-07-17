class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.prev_player = None
        self.next_player = None
        self.in_round = True

    def get_name(self):
        return self.name

    def get_chips(self):
        return self.chips

    def get_hand(self):
        return self.hand

    def get_prev_player(self):
        return self.prev_player

    def get_next_player(self):
        return self.next_player
    
    def get_in_round(self):
        return self.in_round

    def set_prev_player(self, player):
        self.prev_player = player

    def set_next_player(self, player):
        self.next_player = player
    
    def set_in_round(self, in_round):
        self.in_round = in_round

    def receive_card(self, card):
        self.hand.append(card)
    
    def reset_hand(self):
        self.hand = []

    def bet(self, amount):
        if amount <= self.chips:
            self.chips -= amount
        else:
            print("ERROR: NOT ENOUGH CHIPS!")

    