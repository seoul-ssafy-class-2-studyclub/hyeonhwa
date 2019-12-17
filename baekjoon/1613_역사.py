# 플로이드 워셜
n, k = map(int, input().split())
case = [['0']*(n+1) for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())
    case[x][y] = '-1'
    case[y][x] = '1'
for z in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            if case[x][z] != '0' and case[x][z] == case[z][y]:
                case[x][y] = case[x][z]
res = []
for _ in range(int(input())):
    c1, c2 = map(int, input().split())
    res.append(case[c1][c2])
print('\n'.join(res))
