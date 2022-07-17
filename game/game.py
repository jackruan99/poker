import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)


from classes.deck import Deck
from classes.player import Player
from classes.round import Round


NUM_PLAYERS = 6
STARTING_CHIPS = 100


def create_players(num_players):
    first_player = Player("player 0", STARTING_CHIPS)
    prev_player = first_player
    for i in range(1, num_players):
        name = f"Player {i}"
        player = Player(name, STARTING_CHIPS)
        player.set_prev_player(prev_player)
        prev_player.set_next_player(player)
        prev_player = player
    first_player.set_prev_player(prev_player)
    prev_player.set_next_player(first_player)
    return first_player


def play_round(round):
    round.preflop()
    round.flop()
    round.turn()
    round.river()


def reset_round(player_node, num_players):
    deck = Deck()
    deck.shuffle()
    player = player_node
    result_num_players = num_players
    for _ in range(num_players):
        player.reset_hand()
        if player.get_chips == 0:
            result_num_players -= 1
            prev_player = player.get_prev_player()
            next_player = player.get_next_player()
            prev_player.set_next_player(next_player)
            next_player.set_prev_player(prev_player)
        player = player.get_next_player()
    return deck, player_node.get_next_player(), result_num_players


def play_game():
    deck = Deck()
    deck.shuffle()

    player_node = create_players(NUM_PLAYERS)
    num_players = NUM_PLAYERS

    round_num = 0
    while round_num < 1:
        round = Round(round_num, deck, player_node)
        play_round(round)
        round_num += 1
        deck, player_node, num_players = reset_round(player_node, num_players)


play_game()
