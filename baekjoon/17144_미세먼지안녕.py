from pprint import pprint

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
idx = [(0, 1), (-1, 0), (0, -1), (1, 0)]
air = []
for x in range(r):
    if board[x][0] == -1:
        air.append((x, 1))
air1 = air[0]
air2 = air[1]
res = 0
while res < t:
    new_board = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                cnt = 0
                for dx, dy in idx:
                    if 0 <= x+dx < r and 0 <= y+dy < c and board[x+dx][y+dy] >= 0:
                        new_board[x+dx][y+dy] += board[x][y]//5
                        cnt += 1
                new_board[x][y] -= (board[x][y]//5) * cnt
    for x in range(r):
        for y in range(c):
            board[x][y] += new_board[x][y]
            new_board[x][y] = board[x][y]

    new_board[air1[0]][0] = -1
    new_board[air2[0]][0] = -1
    new_board[air1[0]][1] = 0
    new_board[air2[0]][1] = 0
    queue1 = [air1]
    i = 0
    dx, dy = idx[i]
    while queue1:
        x, y = queue1.pop()
        if 0 <= x+dx < r and 0 <= y+dy < c:
            if x+dx == air1[0] and y+dy == 0:
                break
            new_board[x+dx][y+dy] = board[x][y]
            queue1.append((x+dx, y+dy))
        else:
            i += 1
            queue1.append((x, y))
            dx, dy = idx[i]

    queue2 = [air2]
    i = 0
    dx, dy = idx[i]
    while queue2:
        x, y = queue2.pop()
        if 0 <= x+dx < r and 0 <= y+dy < c:
            if x+dx == air2[0] and y+dy == 0:
                break
            new_board[x+dx][y+dy] = board[x][y]
            queue2.append((x+dx, y+dy))
        else:
            i -= 1
            queue2.append((x, y))
            dx, dy = idx[i]

    board = new_board
    res += 1
ans = 0
for i in range(r):
    ans += sum(board[i])
print(ans+2)
