from collections import deque
import sys

sys.setrecursionlimit(1000000000)

def island(x, y):
    global islands
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] == '#':
                board[x+dx][y+dy] = cnt
                queue.append((x+dx, y+dy))
                islands[cnt].append((x+dx, y+dy))


def safety(x, y, value, l=[]):
    for dx, dy in idx:
        if visit[x+dx][y+dy] == False and 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] == '.':
            if x+dx == 0 or x+dx == N-1 or y+dy == 0 or y+dy == M-1:
                return True
            visit[x+dx][y+dy] = True
            safety(x+dx, y+dy, value, l)
            visit[x+dx][y+dy] = False
        if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] != '.' and board[x+dx][y+dy] not in l and board[x+dx][y+dy] != value:
            if dp[board[x+dx][y+dy]] == 0:
                safety(x+dx, y+dy, board[x+dx][y+dy], l)
            if dp[board[x+dx][y+dy]] == 'O':
                l.append(board[x+dx][y+dy])
    if len(l) == 1:
        dp[value] = 'X'
    else:
        dp[value] = 'O'
    return False


def possible():
    for i in range(1, cnt):
        if islands[i] and dp[i] == 0:
            for x, y in islands[i]:
                if safety(x, y, board[x][y]):
                    dp[i] = 'O'
                    break


N, M = map(int, input().split())
board = [[i for i in input()] for _ in range(N)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 1
islands = [[] for _ in range(2000)]
for x in range(N):
    for y in range(M):
        if board[x][y] == '#':
            board[x][y] = cnt
            islands[cnt].append((x, y))
            island(x, y)
            cnt += 1
visit = [[False]*M for _ in range(N)]
dp = [0 for _ in range(cnt)]
possible()
for x in range(N):
    string = ''
    for y in range(M):
        if board[x][y] != '.':
            string += dp[board[x][y]]
        else:
            string += board[x][y]
    print(string)