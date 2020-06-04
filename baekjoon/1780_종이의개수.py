import sys
input = lambda: sys.stdin.readline().rstrip()

def divide(a, b, k):
    num = board[a][b]
    if k == 1:
        res[num+1] += 1
        return
    flag = 0
    for x in range(a, a+k):
        for y in range(b, b+k):
            if num != board[x][y]:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        divide(a, b, k // 3)
        divide(a, b + k//3, k//3)
        divide(a, b + 2*k//3, k//3)
        divide(a + k//3, b, k//3)
        divide(a+2*k//3, b, k//3)
        divide(a+k//3, b+k//3, k//3)
        divide(a+k//3, b+2*k//3, k//3)
        divide(a+2*k//3, b+k//3, k//3)
        divide(a+2*k//3, b+2*k//3, k//3)
    else:
        res[num+1] += 1
        return


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = [0, 0, 0]
divide(0, 0, n)
print('\n'.join(list(map(str, res))))