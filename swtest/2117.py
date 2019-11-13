import sys
sys.stdin = open('input7.txt', 'r')
from collections import deque

def home(i, j):
    global res
    k = 1
    gain = 0
    canget = 0
    house = deque()
    house.append((i, j))
    totalhouse = [(i, j)]
    cnt = 0
    while k <= N+10:
        cost = k**2 + (k-1)**2
        for x, y in house:
            if city[x][y] == 1:
                cnt +=1
        gain = cnt * M - cost
        if gain >= 0:
            if cnt > res:
                res = cnt
        k += 1
        for i in range(len(house)):
            x, y = house.popleft()
            for dx, dy in idx:
                if 0 <= x+dx < N and 0 <= y+dy < N and (x+dx, y+dy) not in totalhouse:
                    totalhouse.append((x+dx, y+dy))
                    house.append((x+dx, y+dy))


for t in range(int(input())):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    idx = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    res = 0
    for i in range(N):
        for j in range(N):
            home(i, j)
    print(f'#{t+1} {res}')
