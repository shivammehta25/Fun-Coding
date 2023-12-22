import math
from collections import Counter, defaultdict
from functools import reduce

from helpers import read_file
from tqdm.auto import tqdm

# data = read_file("inputs/day7_test.txt")
data = read_file("inputs/day7.txt")

def formatter():
    hands, bids = [], []
    for line in data:
        hand, bid = line.split(" ")
        hands.append(hand)
        bids.append(bid)
        
    return hands, bids


def A():
    hands, bids = formatter()
    
    ORDER = {
        'A': 'A',
        'K': 'B',
        'Q': 'C',
        'J': 'D',
        'T': 'E',
        '9': 'F',
        '8': 'G',
        '7': 'H',
        '6': 'I',
        '5': 'J',
        '4': 'K',
        '3': 'L',
        '2': 'M'
    }

    RANKING = {
        "5OFAKIND": [],
        "4OFAKIND": [],
        "FULLHOUSE": [],
        "3OFKIND": [],
        "2PAIR": [],
        "ONEPAIR": [],
        "HIGHCARD": []
    }
    for i, hand in enumerate(hands):
        count = defaultdict(int)
        for card in hand:
            count[card] += 1
        print(count)
        num_values = count.values()
        print(num_values)
        if 5 in num_values:
            RANKING["5OFAKIND"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        elif 4 in num_values:
            RANKING["4OFAKIND"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        elif 3 in num_values and 2 in num_values:
            RANKING["FULLHOUSE"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        elif 3 in num_values:
            RANKING["3OFKIND"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        elif sorted(num_values) == [1, 2, 2]:
            RANKING["2PAIR"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        elif 2 in num_values:
            RANKING["ONEPAIR"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        else:
            RANKING["HIGHCARD"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        
    values = [(None, None) for _ in range(len(RANKING.values()))]
    rank = 1
    total = 0
    for (k, v) in reversed(RANKING.items()):
        v.sort(key=lambda x: x[2])
        print(k, v)
        while v:
            hand, bid, _ = v.pop()
            total += rank*int(bid)
            rank += 1

    print(total)
        

def B():
    hands, bids = formatter()
    
    ORDER = {
        'A': 'A',
        'K': 'B',
        'Q': 'C',
        # 'J': 'D',
        'T': 'E',
        '9': 'F',
        '8': 'G',
        '7': 'H',
        '6': 'I',
        '5': 'J',
        '4': 'K',
        '3': 'L',
        '2': 'M',
        'J': 'N',
    }

    RANKING = {
        "5OFAKIND": [],
        "4OFAKIND": [],
        "FULLHOUSE": [],
        "3OFKIND": [],
        "2PAIR": [],
        "ONEPAIR": [],
        "HIGHCARD": []
    }
    for i, hand in enumerate(hands):
        count = defaultdict(int)
        j = 0
        for card in hand:
            if card == "J":
                j +=1
                continue
            count[card] += 1
        
        if count: 
            max_key = max(count, key=count.get)
            count[max_key] += j
        else:
            count["J"] = j
        
        # print(count)
        num_values = count.values()
        print(num_values)
        if 5 in num_values or ():
            RANKING["5OFAKIND"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        elif 4 in num_values:
            RANKING["4OFAKIND"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        elif 3 in num_values and 2 in num_values:
            RANKING["FULLHOUSE"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        elif 3 in num_values:
            RANKING["3OFKIND"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        elif sorted(num_values) == [1, 2, 2]:
            RANKING["2PAIR"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        elif 2 in num_values:
            RANKING["ONEPAIR"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        else:
            RANKING["HIGHCARD"].append((hand, bids[i], "".join(map(str, [ORDER[card] for card in hand]))))
        
    values = [(None, None) for _ in range(len(RANKING.values()))]
    rank = 1
    total = 0
    for (k, v) in reversed(RANKING.items()):
        v.sort(key=lambda x: x[2])
        print(k, v)
        while v:
            hand, bid, _ = v.pop()
            total += rank*int(bid)
            rank += 1

    print(total)
            

if __name__ == "__main__":
    # A()
    B()