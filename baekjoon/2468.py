from pprint import pprint

def rain(arr, x):
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= x:
                arr[i][j] = -1


def findsafety(arr, x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in idx:
            xi = x + dx
            yi = y + dy
            if 0 <= xi < N and 0 <= yi < N and arr[xi][yi] > 0:
                queue.append((xi, yi))
                arr[xi][yi] = 0
    return 1


def findmax(arr):
    s = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > s:
                s = arr[i][j]
    return s


N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
s = findmax(city)
idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
k = 0
for x in range(s+1):
    newcity = [i[:] for i in city]
    rain(newcity, x)
    res = 0
    visit = False
    for i in range(N):
        for j in range(N):
            if newcity[i][j] > 0:
                res += findsafety(newcity, i, j)
                visit = True
    if res > k:
        k = res
    if not visit:
        break
print(k)