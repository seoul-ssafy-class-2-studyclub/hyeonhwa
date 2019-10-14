def direction(d):
    if d == 1:
        return (-1, 0)
    elif d == 2:
        return (1, 0)
    elif d == 3:
        return (0, 1)
    else:
        return (0, -1)


def catch(x):
    global res
    fish = 1
    while fish <= R:
        if board[fish][x]:
            res += board[fish][x][2]
            board[fish][x] = []
            break
        fish += 1
    fish_arrival(fishes)


def fish_move(i, j, fish):
    cnt = 0
    x, y = i, j
    dx, dy = direction(board[i][j][1])
    while cnt < board[i][j][0]:
        if 1 <= x+dx <= R and 1 <= y+dy <= C:
            x += dx
            y += dy
            cnt += 1
        if dx:
            if x+dx == 0 or x+dx == R+1:
                if board[i][j][1] == 1:
                    board[i][j][1] = 2
                elif board[i][j][1] == 2:
                    board[i][j][1] = 1
            dx, dy = direction(board[i][j][1])
        elif dy:
            if y+dy == 0 or y+dy == C+1:
                if board[i][j][1] == 3:
                    board[i][j][1] = 4
                elif board[i][j][1] == 4:
                    board[i][j][1] = 3
            dx, dy = direction(board[i][j][1])
        if cnt >= board[i][j][0]:
            fish.append([x, y, board[i][j][0], board[i][j][1], board[i][j][2]])
            board[i][j] = []
            break


def fish_arrival(arr):
    global fishes
    fish = []
    for x, y, s, d, z in fishes:
        if board[x][y]:
            fish_move(x, y, fish)
    for x, y, s, d, z in fish:
        if board[x][y]:
            if z > board[x][y][2]:
                board[x][y] = [s, d, z]
        else:
            board[x][y] = [s, d, z]
    fishes = fish


R, C, M = map(int, input().split())
board = [[[] for _ in range(C+1)] for __ in range(R+1)]
fishes = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r][c] = [s, d, z]
    fishes.append([r, c, s, d, z])
res = 0
for x in range(1, C+1):
    catch(x)
print(res)