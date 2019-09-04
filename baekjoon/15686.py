import sys

sys.setrecursionlimit(10000)

def chickenroad(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def findchicken(arr):
    chicken = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                chicken += [[i, j]]
    return chicken


def findpeople(arr):
    house = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                house += [[i, j]]
    return house


def m_road(arr, x, y):
    s = 2*N
    for dx, dy in arr:
        k = chickenroad(x, y, dx, dy)
        if s > k:
            s = k
    return s


def combination(arr=[], idx=-1):
    if len(arr) == M:
        res.append(arr)
        return 0
    for i in range(idx+1, len(chicken)):
        combination(arr+[chicken[i]], i)
            

N, M = map(int, input().split())
city = [list(map(int, input().split()))for _ in range(N)]
chicken = findchicken(city)
house = findpeople(city)
res = []
combination()
s = 100000000000
for i in res:
    total_chicken = 0
    for x, y in house:
        total_chicken += m_road(i, x, y)
    if s > total_chicken:
        s = total_chicken
print(s)

