import sys

sys.stdin = open('점심.txt', 'r')

def gostairs(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def findstairs(arr):
    stairs = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2:
                stairs += [[i, j, board[i][j]]]
    return stairs


def findpoeple(arr):
    people = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                people += [[i, j]]
    return people


def order(arr, sx, sy):
    go = []
    for px, py in arr:
        k = gostairs(px, py, sx, sy)
        go.append(k)
    go.sort()
    return go


def down(arr, x, wait, s):
    global time
    m = time
    if not arr:
        return 0
    flag = 0
    if wait:
        for i in wait[:]:
            if len(s) < 3:
                s.append(i)
                wait.remove(i)
    for i in range(len(arr)):
        arr[i] -= 1
        if arr[i] < 0:
            arr[i] = 0
    if s:
        for i in range(len(s)):
            s[i] -= 1
        for i in s[:]:
            if i == -x-1:
                s.remove(i)
                if wait:
                    while wait and len(s) < 3:
                        s.append(wait.pop(0)-1)
    for i in arr[:]:
        if i == 0:
            wait.append(arr.pop(i))
    time += 1
    if not arr:
        l = len(wait)
        if s and l+len(s) > 3:
            if len(s)-1 < l-1:
                time += (s[-1]+x) + x
            else:
                time += (s[l-1]+x) + x
        elif l + len(s) <= 3:
            time += x
        elif not s:
            time += x
    down(arr, x, wait, s)
    


T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split()))for _ in range(N)]
    stairs = findstairs(board)
    people = findpoeple(board)
    l = len(people)
    res = []
    for i in range(1<<l):
        first = []
        last = []
        for j in range(l):
            if i & (1<<j):
                first.append(people[j])
            else:
                last.append(people[j])
        x1, y1, k1 = stairs[0]
        gos = order(first, x1, y1)
        x2, y2, k2 = stairs[1]
        gos2 = order(last, x2, y2)
        time = 1
        down(gos, k1, [], [])
        m = time
        time = 1
        down(gos2, k2, [], [])
        if m > time:
            res.append(m)
        else:
            res.append(time)
    # print(res)
    print('#{} {}'.format(t+1, min(res)))
