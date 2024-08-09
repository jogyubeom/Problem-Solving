
import collections

N = int(input())
cards = list(range(1, N+1))
cards = collections.deque(cards)
while len(cards) != 1:
    cards.popleft()
    first = cards.popleft()
    cards.append(first)
print(cards[0])
