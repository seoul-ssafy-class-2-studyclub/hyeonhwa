from collections import deque
from pprint import pprint
def find4(x, y, arr):
    global locy
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < 12 and 0 <= y+dy < 6 and board[x+dx][y+dy] == board[x][y]:
                if (x+dx, y+dy) not in arr:
                    arr.append((x+dx, y+dy))
                    queue.append((x+dx, y+dy))
    if len(arr) >= 4:
        for i, j in arr:
            board[i][j] = '.'
        return 1
    return 0


def down():
    for y in range(6):
        k = 11
        a = 0
        arr = [0]*12
        while k >= 0:
            if board[k][y] != '.':
                arr[a] = board[k][y]
                board[k][y] = '.'
                a += 1
            k -= 1
        for x in range(a):
            if arr[x] != 0:
                board[11-x][y] = arr[x]

def con():
    cnt = 0
    while True:
        flag = 0
        res = 0
        for i in range(11, -1, -1):
            for j in range(6):
                if board[i][j] != '.':
                    res = find4(i, j, [])
                    if res:
                        flag = 1
        cnt += 1
        # pprint(board)
        down()
        # pprint(board)
        if flag == 0:
            break
    return cnt


board = [[i for i in input()] for _ in range(12)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = con()-1
print(res)
