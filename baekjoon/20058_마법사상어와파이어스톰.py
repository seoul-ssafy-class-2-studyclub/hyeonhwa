from pprint import pprint

def rotate(m):
    new = [[0]*2**n for _ in range(2**n)]
    for i in range(0, 2**n, m):
        for j in range(0, 2**n, m):
            for ii in range(i, i+m):
                k = i
                for jj in range(j, j+m):
                    new[k][i+j+m-1-ii] = board[ii][jj]
                    k += 1
    return new


def melt():
    melting = []
    idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x in range(2**n):
        for y in range(2**n):
            if board[x][y] > 0:
                flag = 0
                for dx, dy in idx:
                    if 0 <= x+dx < 2**n and 0 <= y+dy < 2**n:
                        if board[x+dx][y+dy] > 0:
                            flag += 1
                if flag < 3:
                    melting.append((x, y))
    for x, y in melting:
        board[x][y] -= 1


n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**n)]
ls = list(map(int, input().split()))
for l in ls:
    board = rotate(2**l)
    melt()
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = [[0]*2**n for _ in range(2**n)]
total, res = 0, 0
for x in range(2**n):
    for y in range(2**n):
        if board[x][y]:
            if not visit[x][y]:
                visit[x][y] = 1
                total += board[x][y]
                queue = [(x, y)]
                for i, j in queue:
                    for dx, dy in idx:
                        if 0 <= i+dx < 2**n and 0 <= j+dy < 2**n and not visit[i+dx][j+dy]:
                            if board[i+dx][j+dy]:
                                queue.append((i+dx, j+dy))
                                visit[i+dx][j+dy] = 1
                                total += board[i+dx][j+dy]
                res = max(res, len(queue))
print(total)
print(res)
