import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(x, arr):
    global cnt
    if len(arr) == 7:
        cnt.append(arr)
        return
    for i in range(x, 25):
        if not visit[i]:
            visit[i] = 1
            dfs(i, arr+[i])
            visit[i] = 0


board = [[i for i in input()] for _ in range(5)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = []
visit = [0]*25
dfs(0, [])
res = 0
for check in cnt:
    nums = [[0]*5 for _ in range(5)]
    xx = check[0] // 5
    yy = check[0] % 5
    path = board[xx][yy]
    queue = [(xx, yy)]
    nums[xx][yy] = 1
    flag = 0
    for x, y in queue:
        for dx, dy in idx:
            if 0 <= x+dx < 5 and 0 <= y+dy < 5 and nums[x+dx][y+dy] == 0 and 5*(x+dx) + y+dy in check:
                path += board[x+dx][y+dy]
                if path.count('Y') >= 4:
                    flag = 1
                    break       
                queue.append((x+dx, y+dy))
                nums[x+dx][y+dy] = 1
        if flag == 1:
            break
    if flag == 0 and len(queue) == 7:
        res += 1
print(res)