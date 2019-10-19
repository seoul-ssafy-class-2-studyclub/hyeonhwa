import collections
import pprint

def canwatch(i, j):
    global k
    direction = cameradirection[board[i][j]]
    queue = collections.deque()
    x, y = i, j
    l = 0
    for idx in direction:
        watch[k][l].add((i, j))
        for dx, dy in idx:
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                if 0 <= x+dx < N and 0 <= y+dy < M and board[x+dx][y+dy] != 6 and l < 4:
                    watch[k][l].add((x+dx, y+dy))
                    queue.append((x+dx, y+dy))
        l += 1


def plus(arr=[], s=set(), idx=0):
    global res
    if len(arr) == len(camera):
        # print(arr)
        if res < len(s):
            res = len(s)
        return
    for i in range(4):
        arr.append(i)
        if watch[len(arr)-1][i] == set():
            arr.pop()
            continue
        plus(arr, s|watch[len(arr)-1][i], i)
        arr.pop()


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cameradirection = {1:[[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]],
2:[[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
3:[[(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)]], 
4:[[(-1, 0), (0, 1), (0, -1)],[(1, 0), (0, 1), (0, -1)], [(-1, 0), (1, 0), (0, -1)], [(-1, 0), (1, 0), (0, 1)]], 
5:[[(-1, 0), (1, 0), (0, 1), (0, -1)]]}

wall = 0
camera = []
watch = [[set() for _ in range(4)] for _ in range(8)]
k = 0
for x in range(N):
    for y in range(M):
        if 0 < board[x][y] < 6 and k < 8:
            canwatch(x, y)
            camera += [k]
            k += 1
        if board[x][y] == 6:
            wall += 1
res = 0
if len(camera) == 1:
    for i in watch[0]:
        res = max(res, len(i))
else:
    # pprint.pprint(watch)
    plus()
res = N*M - res- wall
print(res)
