import collections

def deal(deck):
    return deck[::-1]

def cut(deck, n):
    if n > 0:
        return deck[n:] + deck[:n]
    else:
        n = abs(n)
        return deck[-n:] + deck[:-n]

def deal_incr(deck, incr):
    pos = 0
    deck = collections.deque(deck)
    s = len(deck)
    new_deck = [None for _ in range(s)]
    while len(deck) > 0:
        new_deck[pos % s] = deck.popleft()
        pos += incr
    return new_deck

deck = [n for n in range(119315717514047+1)]
for line in open("../input/22", "r").readlines():
    if "cut" in line:
        deck = cut(deck, int(line.split(" ")[-1]))
    elif "increment" in line:
        deck = deal_incr(deck, int(line.split(" ")[-1]))
    elif "new stack" in line:
        deck = deal(deck)
    else:
        print("nothing to do", line)
