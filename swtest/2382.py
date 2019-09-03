from pprint import pprint
import sys
sys.stdin = open('input1.txt', 'r')

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
        crush += [[newboard[x+dx][y+dy], board[x][y], [x+dx, y+dy]]]

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
        crush.sort(key=lambda x:x[0])
        crushes = []
        for i in range(len(crush)-1):
            if crush[i+1][0] == crush[i][0]:
                if crushes and crushes[-1][0] == crush[i+1][0]:
                    crushes[-1].insert(-2, crush[i+1][1])
                else:
                    crushes += [[crush[i][0], crush[i][1], crush[i+1][1], crush[i][-1]]]
        if crushes:
            for i in crush[:]:
                for j in range(len(crushes)):
                    if crushes[j][0] in i:
                        crush.remove(i)
        for i in range(len(crushes)):
            z, a = 0, []
            for j in range(len(crushes[i])-1):
                z += crushes[i][j][1]
                a += [crushes[i][j]]
            a.sort(key=lambda x:x[1])
            m = a[-1][0]
            newboard[crushes[i][-1][0]][crushes[i][-1][1]] = [m, z]
            for j in newk:
                if j[0] == crushes[i][-1][0] and crushes[i][-1][1] == j[1]:
                    j[2] = z
                    j[3] = m
                    break
        for i in range(len(crush)):
            z, a = 0, []
            for j in range(len(crush[i])-1):
                z += crush[i][j][1]
                a += [crush[i][j]]
            a.sort(key=lambda x:x[1])
            m = a[-1][0]
            newboard[crush[i][-1][0]][crush[i][-1][1]] = [m, z]
            for j in newk:
                if j[0] == crush[i][-1][0] and crush[i][-1][1] == j[1]:
                    j[2] = z
                    j[3] = m
                    break
        year += 1
        board = newboard
        k = newk
    res = 0
    for x in k:
        res += x[2]
    print('#{} {}'.format(t+1, res))