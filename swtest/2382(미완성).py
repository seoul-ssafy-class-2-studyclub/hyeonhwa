from pprint import pprint

'''
1
7 2 9
1 1 7 1
2 1 7 1
5 1 5 4
3 2 8 4
4 3 14 1
3 4 3 3
1 5 8 2
3 5 100 1
5 5 1 1
'''

def move(x, y):
    for k in K:
        m = k[-1]
        if m == 1:
            dx, dy = idx[0]
            while 0 <= x+dx < N and 0 <= y+dy < N:
                if board[x+dx][y+dy] == 0:
                    board[x+dx][y+dy] = board[x][y]
                    board[x][y] = 0
                elif board[x+dx][y+dy] > 0:
                    if board[x+dx][y+dy] > board[x][y]:
                        board[x+dx][y+dy] = board[x][y] + board[x+dx][y+dy]
                        board[x][y] = 0
                        # m 지정
                        break
                    else:
                        board[x+dx][y+dy] = board[x][y] + board[x+dx][y+dy]
                        board[x][y] = 0
                elif board[x+dx][y+dy] == -1:
                    board[x][y] //= 2
                    m = 2
                    break
                x = x+dx
                y = y+dy
        if m == 2:
            dx, dy = idx[1]
            while 0 <= x+dx < N and 0 <= y+dy < N:
                board[x+dx][y+dy] = board[x][y]
                board[x][y] = 0
                x = x+dx
                y = y+dy
        if m == 3:
            dx, dy = idx[2]
            while 0 <= x+dx < N and 0 <= y+dy < N and board[x+dx][y+dy] != -1:
                board[x+dx][y+dy] = board[x][y]
                board[x][y] = 0
                x = x+dx
                y = y+dy
        if m == 4:
            dx, dy = idx[3]
            while 0 <= x+dx < N and 0 <= y+dy < N and board[x+dx][y+dy] != -1:
                board[x+dx][y+dy] = board[x][y]
                board[x][y] = 0
                x = x+dx
                y = y+dy


T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    k = [list(map(int, input().split())) for _ in range(K)] # 상 1 하 2 좌 3 우 4
    board = [[0 for _ in range(N)] for __ in range(N)]
    board[0], board[-1] = [-1 for _ in range(N)], [-1 for _ in range(N)]
    for i in range(N):
        board[i][0] = -1
        board[i][-1] = -1
    for i in k:
        board[i[0]][i[1]] = i[2] # 초기 미생물이 존재하는 board
    idx = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 이동 index , 상하좌우
    