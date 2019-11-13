def fun():
    arr = []
    grow.sort(key=lambda x:x[2])
    while grow:
        x, y, z = grow.pop()
        for dx, dy in idx:
            if board[x+dx][y+dy] == 0:
                arr.append((x+dx, y+dy, z))
                board[x+dx][y+dy] = z
    return arr


T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    board = [[0 for _ in range(1001)] for __ in range(1001)]
    cells = []
    for i in range(N):
        for j in range(M):
            board[i+(501-N//2)][j+(501-M//2)] = grid[i][j]
            if grid[i][j] != 0:
                cells.append((i+(501-N//2),j+(501-M//2), grid[i][j]))
    k = 0
    grow = []
    while k < K:
        arr = fun()
        for i in range(len(cells)-1, -1, -1):
            x, y, n = cells[i]
            if board[x][y] > 0:
                board[x][y] -= 1
            if board[x][y] == 0:
                board[x][y] = -1
                grow.append(cells[i])
            elif board[x][y] < 0:
                board[x][y] -= 1
            if board[x][y] == -(n+1):
                cells.pop(i)
        k += 1
        cells.extend(arr)
    print(f'#{t+1} {len(cells)}')
