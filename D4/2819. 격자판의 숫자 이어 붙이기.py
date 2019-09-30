def cnt(x, y, r=''):
    if len(r) == 7:
        res.add(r)
        return
    for dx, dy in idx:
        if 0 <= x+dx < 4 and 0 <= y+dy < 4: 
            cnt(x+dx, y+dy, r+board[x][y])
            

T = int(input())
for t in range(T):
    board = [list(input().split()) for _ in range(4)]
    idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    res = set()
    for x in range(4):
        for y in range(4):
            cnt(x, y)
    print(f'#{t+1} {len(res)}')