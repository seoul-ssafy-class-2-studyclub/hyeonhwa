def blackjack(s=0, cnt=0, i=0):
    global res
    if cnt == 3:
        if res < s <= M:
            res = s
    if i < N and cnt < 3:
        temp = s + cards[i]
        if temp <= M:
            blackjack(temp, cnt+1, i+1)
        blackjack(s, cnt, i+1)


N, M = map(int, input().split())
cards = list(map(int, input().split()))
res = 0
blackjack()
print(res)
