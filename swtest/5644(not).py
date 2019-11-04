import sys
# sys.stdin = open('charge.txt', 'r')

def movediff(x, y):
    res = []
    for cy, cx, c, p in charger:
        if abs(x-cx) + abs(y-cy) <= c:
            res.append((cx, cy, p))
    return res
    

def moves():
    global res
    x1, y1 = 1, 1
    x2, y2 = 10, 10
    i = 0
    while i <= M:
        l1 = movediff(x1, y1)
        l1.sort(key=lambda x:x[2], reverse=True)
        l2 = movediff(x2, y2)
        l2.sort(key=lambda x:x[2], reverse=True)
        if i < M:
            dx1, dy1 = idx[first_moves[i]]
            dx2, dy2 = idx[last_moves[i]]
            if 0 <= x1+dx1 < 11 and 0 <= y1+dy1 < 11:
                x1 += dx1
                y1 += dy1
            if 0 <= x2+dx2 < 11 and 0 <= y2+dy2 < 11:
                x2 += dx2
                y2 += dy2
        i += 1
        if not l1 and not l2:
            continue
        if l1 and not l2:
            res += l1[0][2]
        elif not l1 and l2:
            res += l2[0][2]
        elif len(l1) == 1 and len(l2) == 1 and l1 == l2:
            res += l1[0][2]
        elif len(l1) == 1 and len(l2) == 1 and l1 != l2:
            res += l1[0][2]
            res += l2[0][2]
        else:
            flag = 0
            for cx, cy, p in l1:
                if (cx, cy, p) in l2:
                    flag = (cx, cy, p)
                    break
            if flag == 0:
                res += l1[0][2]
                res += l2[0][2]
            else:
                if len(l1) == 1:
                    for p in l2:
                        if flag != p:
                            res += p[2]
                            break
                    res += l1[0][2]
                elif len(l2) == 1:
                    for p in l1:
                        if flag != p:
                            res += p[2]
                            break
                    res += l2[0][2]
                else:
                    for p in l1:
                        if flag != p:
                            res += p[2]
                            break
                    for p in l2:
                        if flag != p:
                            res += p[2]
                            break


T = int(input())
for t in range(T):
    M, A = map(int, input().split())
    first_moves = list(map(int, input().split()))
    last_moves = list(map(int, input().split()))
    board = [[0 for _ in range(11)] for _ in range(11)]
    idx = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
    charger = [list(map(int, input().split())) for _ in range(A)]
    res = 0
    moves()
    print(f'#{t+1} {res}')
