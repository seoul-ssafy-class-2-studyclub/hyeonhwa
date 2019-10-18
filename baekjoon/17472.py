import collections
import heapq    
from pprint import pprint

def island(x, y):
    queue = collections.deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] == 1:
                board[x+dx][y+dy] = cnt
                queue.append((x+dx, y+dy))


def findnear(x, y, value):
    global near
    queue = collections.deque()
    for dx, dy in idx:
        queue.append((x, y))
        l = 0
        while queue:
            i, j = queue.popleft()
            if 0 <= i+dx < N and 0 <= j+dy < M and board[i+dx][j+dy] == 0:
                queue.append((i+dx, j+dy))
                l += 1
            if 0 <= i+dx < N and 0 <= j+dy < M and board[i+dx][j+dy] != 0 and board[i+dx][j+dy] != value:
                if not near:
                    near[value] += [[board[i+dx][j+dy], l]]
                if near:
                    flag = 0
                    for k in near:
                        if board[i+dx][j+dy] in k:
                            flag = 1
                            if k[1] > l:
                                k[1] = l
                    if flag == 0:
                        near[value] += [[board[i+dx][j+dy], l]]
                break


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 2
for x in range(N):
    for y in range(M):
        if board[x][y] == 1:
            board[x][y] = cnt
            island(x, y)
            cnt += 1
near = [[] for _ in range(cnt)]
for x in range(N):
    for y in range(M):
        if board[x][y] != 0:
            findnear(x, y, board[x][y])
# print(near)
INF = float('inf')
cost = [INF]*cnt
cost[2] = 0
visit = [False]*cnt
queue = []
heapq.heappush(queue, (0, 2))
while queue:
    value, node = heapq.heappop(queue)
    visit[node] = True
    for n, v in near[node]:
        if visit[n]:
            continue
        if v < 2:
            continue
        if cost[n] > v:
            cost[n] = v
            heapq.heappush(queue, (v, n))
if INF in cost[2:]:
    print(-1)
else:
    print(sum(cost[2:]))
# print(visit)