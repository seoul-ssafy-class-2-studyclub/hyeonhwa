from pprint import pprint
# import sys
# sys.stdin = open('input1.txt', 'r')

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
    global newk
    global crush
    m = board[x][y][0]
    dx, dy = idx[m-1]
    if 0 < x+dx < N-1 and 0 < y+dy < N-1 and newboard[x+dx][y+dy] == []:
        newboard[x+dx][y+dy] = [m, board[x][y][-1]]
        board[x][y] = []
        newk += [[x+dx, y+dy, newboard[x+dx][y+dy][-1], m]]
    elif x+dx == 0 or y+dy == 0 or x+dx == N-1 or y+dy == N-1:
        if board[x][y][-1]//2 != 0:
            if m == 1:
                newboard[x+dx][y+dy] = [2, board[x][y][-1]//2]
                newk += [[x+dx, y+dy, newboard[x+dx][y+dy][-1], 2]]
            elif m == 2:
                newboard[x+dx][y+dy] = [1, board[x][y][-1]//2]
                newk += [[x+dx, y+dy, newboard[x+dx][y+dy][-1], 1]]
            elif m == 3:
                newboard[x+dx][y+dy] = [4, board[x][y][-1]//2]
                newk += [[x+dx, y+dy, newboard[x+dx][y+dy][-1], 4]]
            elif m == 4:
                newboard[x+dx][y+dy] = [3, board[x][y][-1]//2]
                newk += [[x+dx, y+dy, newboard[x+dx][y+dy][-1], 3]]
        board[x][y] = []
    elif 0 < x+dx < N-1 and 0 < y+dy < N-1 and newboard[x+dx][y+dy] != []:
        crush += [board[x][y]]
        k = board[x][y][-1] + newboard[x+dx][y+dy][-1]
        if newboard[x+dx][y+dy][-1] < board[x][y][-1]:
            newboard[x+dx][y+dy] = [m, k]
        else:
            newboard[x+dx][y+dy] = [newboard[x+dx][y+dy][0], k]
        board[x][y] = []
        newk += [[x+dx, y+dy, newboard[x+dx][y+dy][-1], newboard[x+dx][y+dy][0]]]
    print(crush)
    # pprint(newboard)
    # print(newk)

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    k = [list(map(int, input().split())) for _ in range(K)] # 상 1 하 2 좌 3 우 4
    board = [[[] for _ in range(N)] for __ in range(N)]
    for i in k:
        board[i[0]][i[1]] = [i[-1], i[2]] # 초기 미생물이 존재하는 board
    idx = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 이동 index , 상하좌우
    year = 0
    while True:
        if year == M:
            break
        newboard = [[[] for _ in range(N)] for __ in range(N)]
        newk = []
        crush = []
        for i in k:
            x = i[0]
            y = i[1]
            if board[x][y] != []:
                move(x, y)
        year += 1
        board = newboard
        k = newk
        # pprint(newboard)
    res = 0
    for x in k:
        res += x[2]
    print('#{} {}'.format(t+1, res))