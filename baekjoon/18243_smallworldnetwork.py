n, k = map(int, input().split())
friends = [[10]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    friends[i][i] = 0
for _ in range(k):
    a, b = map(int, input().split())
    friends[a][b] = 1
    friends[b][a] = 1
for z in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            if friends[x][y] > friends[x][z] + friends[z][y]:
                friends[x][y] = friends[x][z] + friends[z][y]
flag = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if friends[i][j] > 6:
            flag = 1
            break
    if flag:
        break
if flag:
    print('Big World!')
else:
    print('Small World!')