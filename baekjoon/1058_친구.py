import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
friends = [[1e10]*n for _ in range(n)]
for x in range(n):
    fr = input()
    for y in range(n):
        if fr[y] == 'Y':
            friends[x][y] = 1
for k in range(n):
    for x in range(n):
        for y in range(n):
            if x != y and friends[x][y] > friends[x][k] + friends[k][y]:
                friends[x][y] = friends[x][k] + friends[k][y]
res = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if 0 < friends[i][j] <= 2:
            cnt += 1
    res = max(res, cnt)
print(res)