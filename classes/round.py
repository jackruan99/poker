SMALL_BLIND = 1
BIG_BLIND = 2


class Round:
    def __init__(self, round_num, deck, first_player):
        self.round_num = round_num
        self.deck = deck
        self.pot = 0
        self.dealer = first_player
        self.small_blind = self.dealer.get_next_player()
        self.big_blind = self.small_blind.get_next_player()
        self.community_cards = []

    def _start_betting_round(self, preflop=False):
        players, bets = [], {}
        player = self.dealer.get_next_player()
        while player != self.dealer:
            if player.get_in_round():
                players.append(player)
            player = player.get_next_player()
        if self.dealer.get_in_round():
            players.append(self.dealer)
        for player in players:
            bets[player] = 0
        if preflop:
            self.small_blind.bet(SMALL_BLIND)
            bets[self.small_blind] = SMALL_BLIND
            self.big_blind.bet(BIG_BLIND)
            bets[self.big_blind] = BIG_BLIND
        return players, bets

    def preflop(self):
        players, bets = self._start_betting_round(True)
        for player in players:
            self.deck.deal_to_player(player)
            self.deck.deal_to_player(player)
        # Betting
        self.pot += sum(bets.values())
        print(f"-- ROUND {self.round_num} --")
        for player in players:
            print(f"[{player.name}] (Chips: {player.chips}) ")
            for card in player.get_hand():
                print(card.get_name())
        print(f"Pot: {self.pot}")

    def _print_community_cards(self):
        s = "Community Cards: [ "
        for card in self.community_cards:
            s += card.get_name() + ' '
        print(s + ']')

    def flop(self):
        players, bets = self._start_betting_round()
        for _ in range(3):
            self.community_cards.append(self.deck.deal())
        self._print_community_cards()
        # Betting
        self.pot += sum(bets.values())
        print(f"Pot: {self.pot}")

    def turn(self):
        players, bets = self._start_betting_round()
        self.community_cards.append(self.deck.deal())
        self._print_community_cards()
        # Betting
        self.pot += sum(bets.values())
        print(f"Pot: {self.pot}")

    def river(self):
        players, bets = self._start_betting_round()
        self.community_cards.append(self.deck.deal())
        self._print_community_cards()
        # Betting
        self.pot += sum(bets.values())
        print(f"Pot: {self.pot}")
