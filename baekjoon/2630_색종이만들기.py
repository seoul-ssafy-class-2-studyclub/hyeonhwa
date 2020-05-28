import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# 분할정복
# 4개로 나뉘어서 쿼드트리라고 불림
def quad_tree(x, y, n):
    global board, white, blue
    color = board[x][y] # 첫 색 = 나머지 색
    flag = False

    for i in range(x, x+n):
        if flag:
            break

        for j in range(y, y+n):
            if board[i][j] != color:
                quad_tree(x, y, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x + n//2, y+n//2, n//2)
                flag = True
                break
    if not flag:
        if not color:
            white += 1
        else: blue += 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
blue = 0
white = 0
total = [(0, 0, n-1, n-1, n)]
quad_tree(0, 0, n)
print(white)
print(blue)
