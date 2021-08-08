cards = [i for i in range(1, 21)]
for _ in range(10):
    s, e = map(int, input().split())
    card = cards[s-1:e]
    card.reverse()
    cards[s-1:e] = card
print(" ".join(list(map(str, cards))))