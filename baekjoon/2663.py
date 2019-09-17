from pprint import pprint


N = int(input())
locations = []
board = [[0 for _ in range(15)] for __ in range(15)]
for _ in range(N//5+1):
    l = list(map(int, input().split()))
    for x in range(0, len(l), 2):
        locations.append((l[x+1], l[x]))
x, y = locations[0][0], locations[0][1]
nx, ny = locations[1][0], locations[1][1]
if x == nx:
    m = min(y, ny)
    for j in range(abs(y-ny)):
        board[x][m+j] = 1
elif y == ny:
    m = min(x, nx)
    for j in range(abs(x-nx)):
        board[m+j][y] = 1
for i in range(1, N-1):
    x, y = locations[i][0], locations[i][1]
    nx, ny = locations[i+1][0], locations[i+1][1]
    if x == nx:
        m = min(y, ny)
        if abs(x-locations[i-1][0]) > 1 and abs(y-ny) > 1:
            for j in range(abs(y-ny)):
                board[x][m+j] = 1
    elif y == ny:
        m = min(x, nx)
        if abs(y-locations[i-1][1]) > 1 and abs(x-nx) > 1:
            for j in range(abs(x-nx)):
                board[m+j][y] = 1
pprint(board)
