import sys
import collections
input = lambda: sys.stdin.readline().rstrip()

def find(i, j, k):
    queue = collections.deque()
    queue.append((i, j, 0))
    visit = [[0]*n for _ in range(n)]
    visit[i][j] = 1
    fishes = []
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < n and 0 <= y+dy < n and visit[x+dx][y+dy] == 0:
                if board[x+dx][y+dy] == 0 or board[x+dx][y+dy] == k:
                    queue.append((x+dx, y+dy, cnt+1))
                    visit[x+dx][y+dy] = 1
                elif 0 < board[x+dx][y+dy] < k:
                    fishes.append((x+dx, y+dy, cnt+1))
                    visit[x+dx][y+dy] = 1
    fishes.sort(key=lambda x:(x[2], x[0], x[1]))
    if not fishes:
        return (-1, -1, -1)
    if board[fishes[0][0]][fishes[0][1]] >= k:
        return (-1, -1, -1)
    return fishes[0]
                 

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
idx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
flag = 0
for x in range(n):
    for y in range(n):
        if board[x][y] == 9:
            babyfish = (x, y)
            board[x][y] = 0
            flag = 1
            break
    if flag:
        break
res = 0
amount = 2
cnt = 0
while True:
    flag = find(babyfish[0], babyfish[1], amount)
    if flag == (-1, -1, -1):
        break
    else:
        cnt += 1
        if cnt == amount:
            amount += 1
            cnt = 0
    res += flag[2]
    babyfish = (flag[0], flag[1])
    board[babyfish[0]][babyfish[1]] = 0
print(res)