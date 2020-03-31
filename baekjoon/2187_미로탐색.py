import sys
input = lambda: sys.stdin.readline().rstrip()

def bfs():
    queue = [(0, 0, 0)]
    for x, y, z in queue:
        z += 1
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < M and visited[x+dx][y+dy] == 0 and board[x+dx][y+dy] == '1':
                if x+dx == N-1 and y+dy == M-1:
                    return z+1
                queue.append((x+dx, y+dy, z))
                visited[x+dx][y+dy] = 1


N, M = map(int, input().split())
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [[i for i in input()] for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = bfs()
print(ans)
