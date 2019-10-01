# import sys
# sys.stdin = open('정사각형.txt', 'r')

def move(i, j, l):
    global res
    cnt = 1
    queue = [(i, j)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < N and board[x][y] + 1 == board[x+dx][y+dy]:
                queue += [(x+dx, y+dy)]
                cnt += 1
        if cnt >= res[1]:
            if cnt > res[1]:
                res = [l, cnt]
            elif res[0] and cnt == res[1]:
                if res[0] > l:
                    res = [l, cnt]


T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    res = [0, 0]
    for i in range(N):
        for j in range(N):
            l = board[i][j]
            move(i, j, l)
    print('#{} {} {}'.format(t+1, res[0], res[1]))
