#! python3
"""Hands:
    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
How many hands does Player 1 win?"""
from os.path import join


def rank(hand):
    cards, colors = [i[0] for i in hand], [i[1] for i in hand]
    values = [VALUES[i] for i in cards]
    isStraight = "".join(sorted(cards, key=lambda x: VALUES[x])) in CARDS
    isFlush = len(set(colors)) == 1
    if isStraight and isFlush:
        return "A" not in cards, -1
    sc = set(cards)
    if len(sc) == 2:
        for i in sc:
            if cards.count(i) == 4:
                rank, value = 2, VALUES[i]
                break
            elif cards.count(i) == 3:
                rank, value = 3, VALUES[i]
                break
        return rank, value
    if isFlush:
        return 4, -1
    if isStraight:
        return 5, max(values)
    if len(sc) == 3:
        for i in sc:
            if cards.count(i) == 3:
                rank, value = 6, VALUES[i]
                break
            elif cards.count(i) == 2:
                rank, value = 7, -1
                break
        try:
            return rank, value
        except NameError:
            pass
    if len(sc) == 4:
        for i in sc:
            if cards.count(i) == 2:
                rank, value = 8, VALUES[i]
                break
        try:
            return rank, value
        except NameError:
            pass
    return 9, max(values)


def does_p1_win(hand):
    handList = hand.split(" ")
    p1, p2 = handList[:5], handList[5:]
    p1r, p1v = rank(p1)
    p2r, p2v = rank(p2)
    if p1r != p2r:
        return p1r < p2r
    else:
        if p1v != p2v:
            return p1v > p2v
        else:
            p1c = [VALUES[i[0]] for i in p1]
            p2c = [VALUES[i[0]] for i in p2]
            for _ in range(5):
                m1, m2 = max(p1c), max(p2c)
                if m1 != m2:
                    return m1 > m2
                p1c.remove(m1)
                p2c.remove(m2)

CARDS = "23456789TJQKA"
VALUES = dict((i, a) for a, i in enumerate(CARDS))

with open(join("..", "files", "p054_poker.txt")) as f:
    hands = f.readlines()
print(sum(map(does_p1_win, hands)))
