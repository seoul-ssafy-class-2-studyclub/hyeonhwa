import sys
import collections
input = lambda: sys.stdin.readline().rstrip()

def right(t, i, j):
    queue = collections.deque()
    queue.append((i, j))
    if t == 3:
        while queue:
            x, y = queue.pop()
            if 0 <= y+1 < 6:
                if right_board[x][y+1] == 0 and right_board[x+1][y+1] == 0:
                    queue.append((x, y+1))
                elif right_board[x][y+1] or right_board[x+1][y+1]:
                    right_board[x][y] = right_board[x+1][y] = 1
            else:
                right_board[x][y] = right_board[x+1][y] = 1
    else:
        while queue:
            x, y = queue.pop()
            if 0 <= y+1 < 6:
                if right_board[x][y+1] == 0:
                    queue.append((x, y+1))
                else:
                    right_board[x][y] = 1
                    if t == 2:
                        right_board[x][y-1] = 1
            else:
                right_board[x][y] = 1
                if t == 2:
                    right_board[x][y-1] = 1
    flag1 = check(y-1, 1)
    if flag1:
        move(y-1, 1)
    flag2 = check(y, 1)
    if flag2:
        move(y, 1)


def down(t, i, j):
    queue = collections.deque()
    queue.append((i, j))
    if t == 2:
        while queue:
            x, y = queue.pop()
            if 0 <= x+1 < 6:
                if down_board[x+1][y] == 0 and down_board[x+1][y+1] == 0:
                    queue.append((x+1, y))
                elif down_board[x+1][y] or down_board[x+1][y+1]:
                    down_board[x][y] = down_board[x][y+1] = 1
            else:
                down_board[x][y] = down_board[x][y+1] = 1
    else:
        while queue:
            x, y = queue.pop()
            if 0 <= x+1 < 6:
                if down_board[x+1][y] == 0:
                    queue.append((x+1, y))
                else:
                    down_board[x][y] = 1
                    if t == 3:
                        down_board[x-1][y] = 1
            else:
                down_board[x][y] = 1
                if t == 3:
                    down_board[x-1][y] = 1
    flag1 = check(x-1, 0)
    if flag1:
        move(x-1, 0)
    flag2 = check(x, 0)
    if flag2:
        move(x, 0)


def check(x, chk):
    global res
    if chk: # right
        for i in range(4):
            if not right_board[i][x]:
                return False
        for i in range(4):
            right_board[i][x] = 0
        res += 1
        return True
    else: # down
        for i in range(4):
            if not down_board[x][i]:
                return False
        for i in range(4):
            down_board[x][i] = 0
        res += 1
        return True


def move(x, chk):
    queue = collections.deque()
    if chk: # right
        for i in range(4):
            if right_board[i][x]:
                queue.append((i, x))
                right_board[i][x] = 0
        while queue:
            a, b = queue.popleft()
            if 0 <= b+1 < 6:
                if right_board[a][b+1]:
                    right_board[a][b] = 1
                    break
                else:
                    queue.append((a, b+1))
        return
    else: # down
        for i in range(4):
            if down_board[x][i]:
                queue.append((x, i))
        while queue:
            a, b = queue.popleft()
            if 0 <= a+1 < 6:
                if down_board[a+1][b]:
                    down_board[a][b] = 1
                else:
                    queue.append((a+1, b))
        return


right_board = [[0]*6 for _ in range(4)]
down_board = [[0]*4 for _ in range(6)]
res = 0
n = int(input())
for _ in range(n):
    # t = 1 -> (x, y)
    # t = 2 -> (x, y), (x, y+1)
    # t = 3 -> (x, y), (x+1, y)
    t, x, y = map(int, input().split())
    right(t, x, y)
    down(t, x, y)
total = 0
for i in range(4):
    for j in range(6):
        if right_board[i][j]:
            total += 1
        if down_board[j][i]:
            total += 1
print(res)
print(total)