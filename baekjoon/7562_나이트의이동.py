import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    l = int(input())
    board = [[0]*l for __ in range(l)]
    nx, ny = map(int, input().split())
    board[nx][ny] = 1
    fx, fy = map(int, input().split())
    if nx == fx and ny == fy:
        res = 0
    else:
        queue = [(nx, ny, 0)]
        idx = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
        flag = 0
        while queue:
            x, y, t = queue.pop(0)
            for dx, dy in idx:
                if 0 <= x+dx < l and 0 <= y+dy < l and board[x+dx][y+dy] == 0:
                    if x+dx == fx and y+dy == fy:
                        flag = 1
                        res = t+1
                        break
                    queue.append((x+dx, y+dy, t+1))
                    board[x+dx][y+dy] = 1
            if flag == 1:
                break
    print(res)