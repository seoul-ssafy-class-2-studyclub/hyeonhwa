from pprint import pprint


def dc(arr):
    res = [arr[-1]]
    for i in range(len(arr)-2, -1, -1):
        rx, ry = arr[i+1]
        x, y = arr[i]
        if abs(rx-x) == 1:
            if rx < x:
                res.append((res[-1][0], res[-1][1]-1))
            else:
                res.append((res[-1][0], res[-1][1]+1))
        else:
            if ry < y:
                res.append((res[-1][0]+1, res[-1][1]))
            else:
                res.append((res[-1][0]-1, res[-1][1]))
    return res


def dragoncurb(x, y, d, k=0, arr=[]):
    # print(arr)
    if k == g:
        for x, y in arr:
            if 0 <= x <= 100 and 0 <= y <= 100:
                board[x][y] = 1
        return
    dx, dy = idx[d]
    if not arr:
        arr = [(x, y), (x+dx, y+dy)]
    newarr = dc(arr)
    if newarr[-1][0] == newarr[-2][0]:
        if newarr[-1][1] > newarr[-2][1]:
            d = curb[0]
        else:
            d = curb[2]
    else:
        if newarr[-1][0] > newarr[-2][0]:
            d = curb[3]
        else:
            d = curb[1]
    arr = arr + newarr[1:]
    dragoncurb(arr[-1][0], arr[-1][1], d, k+1, arr)


N = int(input())
idx = {0:(0, 1), 1:(-1, 0), 2:(0, -1), 3:(1, 0)}
curb = {0:1, 1:2, 2:3, 3:0}
board = [[0]*101 for _ in range(101)]
for _ in range(N):
    y, x, d, g = map(int, input().split())
    if g == 0:
        dx, dy = idx[d]
        board[x][y] = 1
        if 0 <= x+dx < 101 and 0 <= y+dy < 101:
            board[x+dx][y+dy] = 1
    else:
        dragoncurb(x, y, d)
cnt = 0
for x in range(100):
    for y in range(100):
        if board[x][y] == board[x+1][y] == board[x][y+1] == board[x+1][y+1] == 1:
            cnt += 1
# pprint(board)
print(cnt)
