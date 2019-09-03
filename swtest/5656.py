import sys
sys.stdin = open('input2.txt', 'r')

def crack(arr, x, y):
    b = arr[x][y]
    i, j = x, y
    if b == 1:
        arr[x][y] = 0
    else:
        for dx, dy in idx:
            cnt = 1
            x, y = i, j
            while 0 <= x < H and 0 <= y < W and cnt <= b:
                arr[x][y] = 0
                x += dx
                y += dy
                cnt += 1
                if 0 <= x < H and 0 <= y < W and cnt <= b and arr[x][y] > 1:
                    crack(arr, x, y)


def reboard(arr):
    dx, dy = 1, 0
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            x, y = i, j
            while 0 <= x+dx < H and 0 <= y+dy < W and arr[x][y] >= 1 and arr[x+dx][y+dy] == 0:
                arr[x+dx][y+dy] = arr[x][y]
                arr[x][y] = 0
                x += dx
                y += dy


def find(arr):
    start = []
    for i in range(W):
        cnt = 0
        while cnt < H and arr[cnt][i] == 0:
            cnt += 1
            if cnt == H:
                break
        if cnt < H:
            start += [[cnt, i]]
    return start


def bfs():
    queue = find(board)
    cnt = 0
    newboard = [[i[:] for i in board] for _ in range(len(queue))]
    while queue:
        if cnt == N:
            break
        nxt = []
        boards = []
        for i in range(len(newboard)):
            crack(newboard[i], queue[i][0], queue[i][1])
            reboard(newboard[i])
            s = 0
            for j in newboard[i]:
                s += j.count(0)
            if s == H * W:
                return 0
            l = len(nxt)
            nxt.extend(find(newboard[i]))
            k = [[j[:] for j in newboard[i]] for _ in range(len(nxt)-l)]
            boards.extend(k)
        queue = nxt
        cnt += 1
        newboard = boards
    return boards


def countlist(arr):
    s = 0
    for i in arr:
        s += i.count(0)
    return H * W - s
    

T = int(input())
for t in range(T):
    N, W, H = map(int, input().split())
    idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    board = [list(map(int, input().split())) for _ in range(H)] # H * W
    idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    reslist = bfs()
    m_sum = H * W
    if reslist == 0:
        print('#{} {}'.format(t+1, reslist))
    else:
        for i in reslist:
            x = countlist(i)
            if m_sum > x:
                m_sum = x
        print('#{} {}'.format(t+1, m_sum))
    