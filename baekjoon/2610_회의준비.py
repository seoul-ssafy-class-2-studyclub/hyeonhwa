n = int(input())
board = [[1e10]*(n+1) for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = 1
    board[b][a] = 1
for i in range(1, n+1):
    board[i][i] = 0
for z in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            if board[x][y] > board[x][z] + board[z][y]:
                board[x][y] = board[x][z] + board[z][y]
check = [0]*(n+1)
connected = []
for i in range(1, n+1):
    s = 0
    con = []
    for j in range(1, n+1):
        if board[i][j] != 1e10:
            con.append(j)
            s = max(s, board[i][j])
    check[i] = s
    con.sort()
    if con not in connected:
        connected.append(con)
res = []
for arr in connected:
    total = 1e10
    node = 0
    for ar in arr:
        if total > check[ar]:
            total = check[ar]
            node = ar
    res.append(node)
res.sort()
print(len(res))
print('\n'.join(list(map(str, res))))