import sys
input = lambda: sys.stdin.readline().rstrip()

def count(x, y):
    queue = [(x, y)]
    for x, y in queue:
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < N and board[x+dx][y+dy] == '1':
                board[x+dx][y+dy] = cnt
                queue.append((x+dx, y+dy))
    return len(queue)


N = int(input())
board = [[i for i in input()] for _ in range(N)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = []
cnt = 2
for x in range(N):
    for y in range(N):
        if board[x][y] == '1':
            board[x][y] = cnt
            res.append(count(x, y))
            cnt += 1
print(str(len(res))+'\n'+'\n'.join(list(map(str, sorted(res)))))