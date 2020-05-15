import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(x, y, arr):
    # global res
    # res = max(len(arr), res)
    # for dx, dy in idx:
    #     if 0 <= x+dx < r and 0 <= y+dy < c and not visit[x+dx][y+dy] and board[x+dx][y+dy] not in arr:
    #         visit[x+dx][y+dy] = 1
    #         dfs(x+dx, y+dy, arr+board[x+dx][y+dy])
    #         visit[x+dx][y+dy] = 0
    queue = [(x, y, arr)]
    res = 0
    while queue:
        x, y, path = queue.pop()
        flag = 0
        for dx, dy in idx:
            if 0 <= x+dx < r and 0 <= y+dy < c:
                if board[x+dx][y+dy] not in path:
                    flag = 1
                    if visit[x+dx][y+dy] != path + board[x+dx][y+dy]:
                        visit[x+dx][y+dy] = path+board[x+dx][y+dy]
                        queue.append((x+dx, y+dy, path+board[x+dx][y+dy]))
        if flag == 0:
            res = max(res, len(path))
    return res


r, c = map(int, input().split())
board = [[i for i in input()] for _ in range(r)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = [[board[0][0] for __ in range(c)] for _ in range(r)]
# visit = [[0]*c for _ in range(r)]
# visit[0][0] = 1
# res = 1
res = dfs(0, 0, board[0][0])
print(res)