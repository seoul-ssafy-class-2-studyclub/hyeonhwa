from pprint import pprint
import collections

def diffuse():
    for i in range(len(city)):
        x, y = city.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < N and board[x+dx][y+dy] == 0:
                city.append((x+dx, y+dy))
                board[x+dx][y+dy] = board[x][y]
                for dxx, dyy in idx:
                    if 0 <= x+dx+dxx < N and 0 <= y+dy+dyy < N and board[x+dx+dxx][y+dy+dyy] != 0 and board[x+dx+dxx][y+dy+dyy] != board[x+dx][y+dy]:
                        citytogether[board[x+dx][y+dy]].add(board[x+dx+dxx][y+dy+dyy])
                        citytogether[board[x+dx+dxx][y+dy+dyy]].add(board[x+dx][y+dy])
            elif 0 <= x+dx < N and 0 <= y+dy < N and board[x+dx][y+dy] != 0 and board[x+dx][y+dy] != board[x][y]:
                citytogether[board[x][y]].add(board[x+dx][y+dy])
                citytogether[board[x+dx][y+dy]].add(board[x][y])


N, K = map(int, input().split())
board = [[0 for _ in range(N)] for __ in range(N)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
city = collections.deque()
citytogether = [set() for _ in range(K+1)]
for i in range(1, K+1):
    y, x = map(int, input().split())
    board[x-1][y-1] = i
    city.append((x-1, y-1))
res = 0
while True:
    flag = 0
    for x in citytogether:
        if len(x) == K-1:
            flag = 1
            break
    if flag == 1:
        break
    res += 1
    diffuse()
print(res)
