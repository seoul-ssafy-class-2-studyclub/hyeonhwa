from pprint import pprint

def gostairs(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def findstairs(arr):
    stairs = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 2:
                stairs += [[i, j, board[i][j]]]
    return stairs


def findpoeple(arr):
    people = []
    cnt = 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                people += [[i, j]]
                cnt += 1
    return people


def order(arr, sx, sy):
    go = []
    for px, py in arr:
        k = gostairs(px, py, sx, sy)
        go.append(k)
    go.sort()
    return go


# def down(arr, x, s=[0]*6, t=0):
    
    
    

T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split()))for _ in range(N)]
    stairs = findstairs(board)
    people = findpoeple(board)
    l = len(people)
    for i in range(1<<l):
        first = []
        last = []
        for j in range(l):
            if i & (1<<j):
                first.append(people[j])
            else:
                last.append(people[j])
        x1, y1, k1 = stairs[0]
        gos = order(first, x1, y1)
        x2, y2, k2 = stairs[1]
        gos2 = order(last, x2, y2)
        print(gos2)
        break
