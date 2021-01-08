def move(x, y, d):
    res = 0
    if d == 0:
        if 0 <= y-1:
            m = board[x][y-1]
            board[x][y-1] = 0
        else:
            return 0
        first = int(0.05*m)
        second = int(0.1*m)
        third = int(0.07*m)
        fourth = int(0.02*m)
        fifth = int(0.01*m)
        if 0 <= y-3:
            board[x][y-3] += first
        else:
            res += first
        if 0 <= x-1 and 0 <= y-2:
            board[x-1][y-2] += second
        else:
            res += second
        if x+1 < n and 0 <= y-2:
            board[x+1][y-2] += second
        else:
            res += second
        if x+1 < n and 0 <= y-1:
            board[x+1][y-1] += third
        else:
            res += third
        if 0 <= x-1 and 0 <= y-1:
            board[x-1][y-1] += third
        else:
            res += third
        if 0 <= x-2 and 0 <= y-1:
            board[x-2][y-1] += fourth
        else:
            res += fourth
        if x+2 < n and 0 <= y-1:
            board[x+2][y-1] += fourth
        else:
            res += fourth
        if 0 <= x-1:
            board[x-1][y] += fifth
        else:
            res += fifth
        if x+1 < n:
            board[x+1][y] += fifth
        else:
            res += fifth
        if 0 <= y-2:
            board[x][y-2] += m - first - 2*(second + third + fourth + fifth)
        else:
            res += m - first - 2*(second + third + fourth + fifth)
    elif d == 1:
        if 0 <= x+1 < n:
            m = board[x+1][y]
            board[x+1][y] = 0
        else:
            return 0
        first = int(0.05*m)
        second = int(0.1*m)
        third = int(0.07*m)
        fourth = int(0.02*m)
        fifth = int(0.01*m)
        if x+3 < n:
            board[x+3][y] += first
        else:
            res += first
        if 0 <= x+2 < n and 0 <= y-1:
            board[x+2][y-1] += second
        else:
            res += second
        if 0 <= x+2 < n and y+1 < n:
            board[x+2][y+1] += second
        else:
            res += second
        if 0 <= x+1 < n and 0 <= y-1:
            board[x+1][y-1] += third
        else:
            res += third
        if 0 <= x+1 < n and y+1 < n:
            board[x+1][y+1] += third
        else:
            res += third
        if 0 <= x+1 < n and 0 <= y-2:
            board[x+1][y-2] += fourth
        else:
            res += fourth
        if 0 <= x+1 < n and y+2 < n:
            board[x+1][y+2] += fourth
        else:
            res += fourth
        if 0 <= y-1:
            board[x][y-1] += fifth
        else:
            res += fifth
        if y+1 < n:
            board[x][y+1] += fifth
        else:
            res += fifth
        if 0 <= x+2 < n:
            board[x+2][y] += m - first - 2*(second + third + fourth + fifth)
        else:
            res += m - first - 2*(second + third + fourth + fifth)
    elif d == 2:
        if 0 <= y+1 < n:
            m = board[x][y+1]
            board[x][y+1] = 0
        else:
            return 0
        first = int(0.05*m)
        second = int(0.1*m)
        third = int(0.07*m)
        fourth = int(0.02*m)
        fifth = int(0.01*m)
        if y+3 < n:
            board[x][y+3] += first
        else:
            res += first
        if 0 <= x-1 and y+2 < n:
            board[x-1][y+2] += second
        else:
            res += second
        if x+1 < n and y+2 < n:
            board[x+1][y+2] += second
        else:
            res += second
        if x+1 < n and y+1 < n:
            board[x+1][y+1] += third
        else:
            res += third
        if 0 <= x-1 and y+1 < n:
            board[x-1][y+1] += third
        else:
            res += third
        if 0 <= x-2 and y+1 < n:
            board[x-2][y+1] += fourth
        else:
            res += fourth
        if x+2 < n and y+1 < n:
            board[x+2][y+1] += fourth
        else:
            res += fourth
        if 0 <= x-1:
            board[x-1][y] += fifth
        else:
            res += fifth
        if x+1 < n:
            board[x+1][y] += fifth
        else:
            res += fifth
        if y+2 < n:
            board[x][y+2] += m - first - 2*(second + third + fourth + fifth)
        else:
            res += m - first - 2*(second + third + fourth + fifth)
    else:
        if 0 <= x-1:
            m = board[x-1][y]
            board[x-1][y] = 0
        else:
            return 0
        first = int(0.05*m)
        second = int(0.1*m)
        third = int(0.07*m)
        fourth = int(0.02*m)
        fifth = int(0.01*m)
        if 0 <= x-3 < n:
            board[x-3][y] += first
        else:
            res += first
        if 0 <= x-2 < n and 0 <= y-1:
            board[x-2][y-1] += second
        else:
            res += second
        if 0 <= x-2 < n and y+1 < n:
            board[x-2][y+1] += second
        else:
            res += second
        if 0 <= x-1 < n and 0 <= y-1:
            board[x-1][y-1] += third
        else:
            res += third
        if 0 <= x-1 < n and y+1 < n:
            board[x-1][y+1] += third
        else:
            res += third
        if 0 <= x-1 < n and 0 <= y-2:
            board[x-1][y-2] += fourth
        else:
            res += fourth
        if 0 <= x-1 < n and y+2 < n:
            board[x-1][y+2] += fourth
        else:
            res += fourth
        if 0 <= y-1:
            board[x][y-1] += fifth
        else:
            res += fifth
        if y+1 < n:
            board[x][y+1] += fifth
        else:
            res += fifth
        if 0 <= x-2 < n:
            board[x-2][y] += m - first - 2*(second + third + fourth + fifth)
        else:
            res += m - first - 2*(second + third + fourth + fifth)
    return res


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
idx = [(0, -1), (1, 0), (0, 1), (-1, 0)]
r, c = n//2, n//2   
cnt, k, d = 1, 1, 0
res = 0
flag = 0
while r or c:
    res += move(r, c, d)
    r, c = r + idx[d][0], c + idx[d][1]
    if k == cnt:
        d = (d+1)%4
        if flag:
            cnt += 1
            flag = 0
        else:
            flag = 1
        k = 0
    k += 1
print(res)
