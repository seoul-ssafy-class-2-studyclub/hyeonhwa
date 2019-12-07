from collections import deque

def princess():
    queue = deque()
    queue.append((0, 0))
    cnt = 0
    gram = 100000
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if visit[x][y] == False:
                visit[x][y] = True
                for dx, dy in idx:
                    if x+dx == N-1 and y+dy == M-1:
                        res = min(cnt+1, gram)
                        return res
                    if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] != 1 and visit[x+dx][y+dy] == False:
                        queue.append((x+dx, y+dy))
                        if board[x+dx][y+dy] == 2:
                            length = abs((N-1)-(x+dx)) + abs((M-1)-(y+dy))
                            gram = cnt + length + 1
        cnt += 1
        if cnt > T:
            return 'Fail'
    return 'Fail'


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = princess()
print(res)
