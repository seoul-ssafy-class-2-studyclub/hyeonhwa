def search(s, x=0, y=0):
    global res
    if s >= res:
        return
    if x == N-1 and y == N-1:
        if res > s:
            res = s
        return
    for dx, dy in idx:
        if 0 <= x+dx < N and 0 <= y+dy < N:
            search(s+board[x+dx][y+dy], x+dx, y+dy)
            

T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    idx = [[1, 0], [0, 1]]
    res = 1000000000
    search(board[0][0])
    print('#{} {}'.format(t+1, res))
