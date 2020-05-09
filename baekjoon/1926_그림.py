import sys
input = lambda: sys.stdin.readline().rstrip()

def area(i, j):
    queue = [(i, j)]
    cnt = 1
    info[i][j] = 1
    for x, y in queue:
        for dx, dy in idx:
            if 0 <= x+dx < n and 0 <= y+dy < m and info[x+dx][y+dy] == '1' and not visit[x+dx][y+dy]:
                info[x+dx][y+dy] = 1
                visit[x+dx][y+dy] = 1
                queue.append((x+dx, y+dy))
                cnt += 1
    return cnt


n, m = map(int, input().split())
info = [list(input().split()) for _ in range(n)]
idx = [(0, -1), (0, 1), (1, 0), (-1, 0)]
visit = [[0 for _ in range(m)] for __ in range(n)]
res = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if info[i][j] == '1':
            visit[i][j] = 1
            res = max(res, area(i, j))
            cnt += 1
print(str(cnt) + '\n' + str(res))