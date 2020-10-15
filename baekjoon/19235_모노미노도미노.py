import sys
import collections
from pprint import pprint
input = lambda: sys.stdin.readline().rstrip()

def move(x, chk):
    t = 1
    if chk: # right
        for i in range(x, -1, -1):
            for j in range(4):
                if right_board[j][i]:
                    if  t == 2:
                        continue
                    value = right_board[j][i]
                    queue = collections.deque()
                    queue.append((j, i))
                    if 0 <= j+1 < 4 and right_board[j][i] == right_board[j+1][i]:
                        t = 2
                        right_board[j][i] = right_board[j+1][i] = 0
                    else:
                        t = 1
                        right_board[j][i] = 0
                    while queue:
                        a, b = queue.popleft()
                        if t == 1:
                            if 0 <= b+1 < 6:
                                if right_board[a][b+1] == 0:
                                    queue.append((a, b+1))
                                else:
                                    right_board[a][b] = value
                            else:
                                right_board[a][b] = value
                        else:
                            if 0 <= b+1 < 6:
                                if right_board[a][b+1] == 0 and right_board[a+1][b+1] == 0:
                                    queue.append((a, b+1))
                                elif right_board[a][b+1] or right_board[a][b+1]:
                                    right_board[a][b] = right_board[a+1][b] = value
                            else:
                                right_board[a][b] = right_board[a+1][b] = value                                   
    else: # down
        for i in range(x, -1, -1):
            for j in range(4):
                if down_board[i][j]:
                    queue = collections.deque()
                    queue.append((i, j))
                    value = down_board[i][j]
                    if 0 <= j+1 < 4 and down_board[i][j+1] == down_board[i][j]:
                        t = 2
                        down_board[i][j+1] = down_board[i][j] = 0
                    else:
                        t = 1
                        down_board[i][j] = 0
                    while queue:
                        a, b = queue.pop()
                        if t == 1:
                            if 0 <= a+1 < 6:
                                if down_board[a+1][b] == 0:
                                    queue.append((a+1, b))
                                else:
                                    down_board[a][b] = value
                            else:
                                down_board[a][b] = value
                        else:
                            if 0 <= a+1 < 6:
                                if down_board[a+1][b] == 0 and down_board[a+1][b+1] == 0:
                                    queue.append((a+1, b))
                                elif down_board[a+1][b] or down_board[a+1][b+1]:
                                    down_board[a][b] = down_board[a][b+1] = value
                            else:
                                down_board[a][b] = down_board[a][b+1] = value


def right(t, i, j, q):
    global res
    queue = collections.deque()
    queue.append((i, 0))
    if t == 3:
        while queue:
            x, y = queue.pop()
            if 0 <= y+1 < 6:
                if right_board[x][y+1] == 0 and right_board[x+1][y+1] == 0:
                    queue.append((x, y+1))
                elif right_board[x][y+1] or right_board[x+1][y+1]:
                    right_board[x][y] = right_board[x+1][y] = q
            else:
                right_board[x][y] = right_board[x+1][y] = q
    else:
        while queue:
            x, y = queue.pop()
            if 0 <= y+1 < 6:
                if right_board[x][y+1] == 0:
                    queue.append((x, y+1))
                else:
                    right_board[x][y] = q
                    if t == 2:
                        right_board[x][y-1] = q
            else:
                right_board[x][y] = q
                if t == 2:
                    right_board[x][y-1] = q
    flag1, flag2 = False, False
    if t == 2:
        flag1 = check(y-1, 1)
    flag2 = check(y, 1)
    if flag1: move(y-1, 1)
    if flag2: move(y, 1)
    cnt = []
    while flag1 or flag2:
        for k in range(5, -1, -1):
            for m in range(4):
                if right_board[m][k] == 0:
                    break
            else:
                for m in range(4):
                    right_board[m][k] = 0
                    cnt.append(k)
        if not cnt:
            flag2 = False
            break
        else:
            for c in cnt:
                move(c, 1)
            res += len(cnt)
            cnt = []
    for a in range(2):
        for b in range(4):
            if right_board[b][a]:
                for c in range(4):
                    right_board[c].pop()
                    right_board[c].insert(0, 0)
                break


def down(t, i, j, q):
    global res
    queue = collections.deque()
    queue.append((0, j))
    if t == 2:
        while queue:
            x, y = queue.pop()
            if 0 <= x+1 < 6:
                if down_board[x+1][y] == 0 and down_board[x+1][y+1] == 0:
                    queue.append((x+1, y))
                elif down_board[x+1][y] or down_board[x+1][y+1]:
                    down_board[x][y] = down_board[x][y+1] = q
            else:
                down_board[x][y] = down_board[x][y+1] = q
    else:
        while queue:
            x, y = queue.pop()
            if 0 <= x+1 < 6:
                if down_board[x+1][y] == 0:
                    queue.append((x+1, y))
                else:
                    down_board[x][y] = q
                    if t == 3:
                        down_board[x-1][y] = q
            else:
                down_board[x][y] = q
                if t == 3:
                    down_board[x-1][y] = q
    flag1, flag2 = False, False
    if t == 3:
        flag1 = check(x-1, 0)
    flag2 = check(x, 0)
    if flag1: move(x-1, 0)
    if flag2: move(x, 0)
    cnt = []
    while flag1 or flag2:
        for k in range(5, -1, -1):
            if down_board[k].count(0) == 0:
                down_board[k] = [0]*4
                cnt.append(k)
        if not cnt:
            flag2 = False
            break
        else:
            for c in cnt:
                move(c, 0)
            res += len(cnt)
            cnt = []
    for a in range(2):
        for b in range(4):
            if down_board[a][b]:
                down_board.pop()
                down_board.insert(0, [0]*4)
                break


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


right_board = [[0]*6 for _ in range(4)]
down_board = [[0]*4 for _ in range(6)]
res = 0
n = int(input())
for i in range(n):
    t, x, y = map(int, input().split())
    right(t, x, y, i+1)
    down(t, x, y, i+1)
total = 0
for i in range(4):
    for j in range(6):
        if right_board[i][j]:
            total += 1
        if down_board[j][i]:
            total += 1
print(res)
print(total)
