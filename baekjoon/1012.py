import collections
import pprint


def grow(x, y):
    board[x][y] = cnt
    queue = collections.deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] == 1:
                board[x+dx][y+dy] = cnt
                queue.append((x+dx, y+dy))


T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    board = [[0]*(M) for _ in range(N)]
    idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    plant = []
    for _ in range(K):
        y, x = map(int, input().split())
        plant.append((x, y))
        board[x][y] = 1
    cnt = 2
    for x, y in plant:
        if board[x][y] == 1:
            grow(x, y)
            cnt += 1
    # pprint.pprint(board)
    print(cnt-2)