from objects.player import Player
from objects.game_round import GameRound


class Game:
    def __init__(self):
        self.players = [Player(f'Player{i}', 100) for i in range(6)]
        self.small_blind_amount = 1
        self.big_blind_amount = 2
        for i in range(100):
            GameRound(i, self.players )