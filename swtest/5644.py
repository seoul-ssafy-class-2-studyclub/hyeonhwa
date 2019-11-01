import collections

def movediff(x, y):
    res = []
    for cx, cy, c, p in charger:
        if abs(x-cx) + abs(y-cy) <= c:
            res.append(((cx, cy, p))
    return res
    

def moves():
    global res
    x1, y1 = 1, 1
    x2, y2 = 10, 10
    i = 0
    while i < M:
        l1 = movediff(x1, y1)
        l2 = movediff(y1, y2)
        dx1, dy1 = idx[first_moves[i]]
        dx2, dy2 = idx[last_moves[i]]
        if 0 <= x1+dx1 < 11 and 0 <= y1+dy1 < 11:
            x1 += dx1
            y1 += dy1
        if 0 <= x2+dx2 < 11 and 0 <= y2+dy2 < 11:
            x2 += dx2
            y2 += dy2
        i += 1


T = int(input())
for t in range(T):
    M, A = map(int, input().split())
    first_moves = list(map(int, input().split()))
    last_moves = list(map(int, input().split()))
    board = [[0 for _ in range(11)] for _ in range(11)]
    idx = [(), (-1, 0), (0, 1), (1, 0), (-1, 0)]
    charger = [list(map(int, input().split())) for _ in range(A)]
    res = 0
