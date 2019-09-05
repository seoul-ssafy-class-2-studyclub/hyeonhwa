import sys
sys.stdin = open('input.txt', 'r')


def findhigh(arr):
    s = 0
    res = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > s:
                res = []
                res = [[i, j]]
                s = arr[i][j]
            elif arr[i][j] == s:
                res += [[i, j]]
    return res


def land(arr, x, y):
    return arr[x][y] - 1


def path(arr, x, y):
    stack = [x, y]
    cnt = 0
    newarr = [i[:] for i in arr]
    visit = [[False]*N for _ in range(N)]
    global K
    m = K
    x = []
    visited = []
    res = []
    while stack:
        l = len(stack)
        j = stack.pop()
        i = stack.pop()
        a = []
        for dx, dy in ix:
            while 0 <= i+dx < N and 0 <= j+dy < N and newarr[i][j] > newarr[i+dx][j+dy]-m:
                visit[i][j] = True
                if newarr[i][j] > newarr[i+dx][j+dy]:
                    stack += [i+dx, j+dy]
                elif newarr[i][j] <= newarr[i+dx][j+dy]:
                    newarr[i+dx][j+dy] = land(newarr, i, j)
                    a += [i+dx, j+dy]
                    m = 0
                break
        cnt += 1
        stack += a
        if l < len(stack):
            for _ in range((len(stack)-l)//2):
                x.append(cnt)
                visited.append(visit)
        elif x and l > len(stack):
            res.append(cnt)
            cnt = x.pop()
            if a:
                p = a.pop()
                o = a.pop()
                if not visit[o][p]:
                    m = K
            visit = visited.pop(0)
            newarr = [i[:] for i in arr]
    res.append(cnt)
    return res


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    idx = findhigh(maps)
    ix = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    res = []
    for x, y in idx:
        res.extend(path(maps, x, y))
    print(max(res))
    # print(res)
