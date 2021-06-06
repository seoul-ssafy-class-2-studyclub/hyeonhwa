def choose(a, b, c, d, e):
    like = []
    empty = []
    cnt_like = 0
    empty = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not board[x][y]:
                flag_like = 0
                flag_empty = 0
                for dx, dy in idx:
                    if 0 <= x+dx < n and 0 <= y+dy < n:
                        if board[x+dx][y+dy] in (b, c, d, e):
                            flag_like += 1
                        if not board[x+dx][y+dy]:
                            flag_empty += 1
                if flag_like > cnt_like:
                    like = [(x, y)]
                elif flag_like == cnt_like and cnt_like != 0:
                    like.append((x, y))
                cnt_like = max(flag_like, cnt_like)
                empty[x][y] = flag_empty
    if len(like) == 1:
        board[like[0][0]][like[0][1]] = a
    elif not len(like):
        cnt = -1
        xx, yy = 0, 0
        for x in range(n):
            for y in range(n):
                if not board[x][y] and cnt < empty[x][y]:
                    cnt = empty[x][y]
                    xx, yy = x, y
        board[xx][yy] = a
    else:
        cnt = -1
        xx, yy = 0, 0
        for x, y in like:
            if cnt < empty[x][y]:
                cnt = empty[x][y]
                xx, yy = x, y
        board[xx][yy] = a


n = int(input())
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [[0]*n for _ in range(n)]
no = []
score = [[] for _ in range(n*n+1)]
for _ in range(n**2):
    a, b, c, d, e = map(int, input().split())
    choose(a, b, c, d, e)
    score[a].extend([b, c, d, e])
res = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in idx:
            if 0 <= x+dx < n and 0 <= y+dy < n and board[x+dx][y+dy] in score[board[x][y]]:
                cnt += 1
        if cnt:
            res += 10**(cnt-1)
print(res)
