# Source: https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python.html/
from collections import defaultdict

card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}

def check_hand(hand):
    # convert hand from list(Card) to list(str)
    hand = [str(card) for card in hand]
    # need to be converted into ["3S", "JC", "QD", "5D", "AH"] for input
    if check_straight_flush(hand):
        return 9
    if check_four_of_a_kind(hand):
        return 8
    if check_full_house(hand):
        return 7
    if check_flush(hand):
        return 6
    if check_straight(hand):
        return 5
    if check_three_of_a_kind(hand):
        return 4
    if check_two_pairs(hand):
        return 3
    if check_one_pair(hand):
        return 2
    return 1

def check_straight_flush(hand):
    return check_flush(hand) and check_straight(hand)

def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False

def check_flush(hand):
    suits = [i[1] for i in hand]
    if len(set(suits))==1:
        return True
    else:
        return False

def check_straight(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range==4):
        return True
    else:
        #check straight with low Ace
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return True
        return False

def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        return True
    else:
        return False

def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False

def check_one_pair(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        return True
    else:
        return False
