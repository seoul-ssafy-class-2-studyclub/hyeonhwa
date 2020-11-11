from collections import deque

def bfs(i):
    queue = deque()
    queue.append(i)
    visit[i] = 1
    cnt = 0
    while queue:
        x = queue.popleft()
        for c in cities[x]:
            if visit[c] == 0:
                visit[c] = 1
                cnt += 1
                queue.append(c)
    return cnt
        

for _ in range(int(input())):
    n, m = map(int, input().split())
    cities = [[] for ___ in range(n+1)]
    visit = [0]*(n+1)
    for __ in range(m):
        a, b = map(int, input().split())
        cities[a].append(b)
        cities[b].append(a)
    res = 0
    for i in range(1, n+1):
        if visit[i] == 0:
            res += bfs(i)
    print(res)
