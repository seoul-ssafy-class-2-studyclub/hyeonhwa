from itertools import permutations

# a = [1, 2, 3, 4, 5, 6]
# print(list(permutations(a, 6)))

# def perm(arr):
#     if len(arr) == 6:
#         print(arr)
#         return
#     for i in range(6):
#         if not visit[i]:
#             visit[i] = 1
#             perm(arr+[i])
#             visit[i] = 0

# visit = [0]*6
# perm([])

def rotate(r, c, s):
    idx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    i = 0
    sx = r-s-1
    sy = c-s-1
    ex = r+s-1
    ey = c+s-1
    new = [[0]*m for _ in range(n)]
    x, y = sx, sy
    while True:
        dx, dy = idx[i]
        if sx <= x+dx <= ex and sy <= y+dy <= ey and not new[x+dx][y+dy]:
            new[x+dx][y+dy] = new_board[x][y]
            x, y = x+dx, y+dy
        else:
            i += 1
            if i == 4:
                i = 0
                sx, sy, ex, ey = sx+1, sy+1, ex-1, ey-1
                if sx >= ex or sy >= ey:
                    if sx == ex and sy == ey:
                        new[sx][sy] = new_board[ex][ey]
                    break
                x, y = sx, sy
    for i in range(r-s-1, r+s):
        for j in range(c-s-1, c+s):
            new_board[i][j] = new[i][j]
    


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
rotate_info = [list(map(int, input().split())) for _ in range(k)]
rotates = list(permutations(rotate_info, k))
res = 1e10
for r in rotates:
    new_board = [board[i][:] for i in range(n)]
    for r, c, s in r:
        rotate(r, c, s)
    for i in range(n):
        res = min(res, sum(new_board[i]))
print(res)
