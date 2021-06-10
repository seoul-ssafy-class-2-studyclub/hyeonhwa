from pprint import pprint

# 블록집합
def group(i, j):
    block = board[i][j]
    queue = [(i, j)]
    visit[i][j] = 1
    zero = 0
    for x, y in queue:
        for dx, dy in idx:
            if 0 <= x+dx < n and 0 <= y+dy < n:
                if (block == board[x+dx][y+dy] or board[x+dx][y+dy] == 0) and not visit[x+dx][y+dy]:
                    queue.append((x+dx,  y+dy))
                    visit[x+dx][y+dy] = 1
                    if board[x+dx][y+dy] == 0:
                        zero +=1
    for a, b in queue:
        if board[a][b] == 0:
            visit[a][b] = 0
    return queue, zero

# 중력
def down():
    for i in range(n):
        for x in range(n-2, -1, -1):
            if board[x][i] >= 0:
                while x < n-1 and board[x+1][i] < -1:
                    board[x+1][i] = board[x][i]
                    board[x][i] = -2
                    x += 1


# 회전
def rotate():
    re_board = [[0]*n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n):
            re_board[n-1-i][j] = board[j][i]
    return re_board


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 0
while True:
    remove_block = []
    remove_zero = 0
    visit = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] > 0 and not visit[x][y]:
                block, zero = group(x, y)
                if len(block) > 1 and len(block) > len(remove_block):
                    remove_block = block
                    remove_zero = zero
                if len(block) > 1 and len(block) == len(remove_block):
                    if zero >= remove_zero:
                        remove_block = block
                        remove_zero = zero
    if not len(remove_block):
        break
    for x, y in remove_block:
        board[x][y] = -2
    res += len(remove_block)**2
    down()
    board = rotate()
    down()
print(res)
