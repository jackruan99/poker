from analysis.check_hand import check_hand

hand_dict = {9:"straight-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"two-pairs", 2:"one-pair", 1:"high-card"}

hand = ["5S", "JS", "TS", "TC", "AS"]
print(hand_dict[check_hand(hand)])