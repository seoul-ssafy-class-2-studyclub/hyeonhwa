import sys
sys.stdin = open('input3.txt', 'r')

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


def path(arr, x, y, cnt, chance):
    global m_cnt
    for dx, dy in idx:
        last = arr[-1]
        if 0 <= x+dx < N and 0 <= y+dy < N:
            if maps[x+dx][y+dy] < last:
                visited[x+dx][y+dy] = True
                path(arr+[maps[x+dx][y+dy]], x+dx, y+dy, cnt+1, chance)
                visited[x+dx][y+dy] = False
            else:
                if not chance and last+K > maps[x+dx][y+dy] and not visited[x+dx][y+dy]:
                    path(arr+[last-1], x+dx, y+dy, cnt+1, True)
    if cnt > m_cnt:
        m_cnt = cnt



T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    ix = findhigh(maps)
    idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    m_cnt = 0
    visited = [[False] * N for _ in range(N)]
    for x, y in ix:
        visited[x][y] = True
        path([maps[x][y]], x, y, 1, False)
        visited[x][y] = False
    print(m_cnt)
    # print(res)
