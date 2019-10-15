from pprint import pprint
from collections import deque

def findmin():
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < N:
                if x+dx == 0 and y+dy == 0:
                    continue
                if board[x+dx][y+dy] > board[x][y]:
                    k = board[x+dx][y+dy] - board[x][y]
                else:
                    k = 0
                if visited[x+dx][y+dy] and visited[x+dx][y+dy] <= visited[x][y]+k+1:
                    continue
                visited[x+dx][y+dy] = visited[x][y] + k + 1
                queue.append((x+dx, y+dy))


T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[0 for _ in range(N)] for __ in range(N)]
    findmin()
    print('#{} {}'.format(t+1, visited[-1][-1]))