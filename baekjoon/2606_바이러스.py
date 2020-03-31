import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
computers = [[] for _ in range(N+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)
visited = [0]*(N+1)
visited[1] = 1
res = 0
queue = [1]
for x in queue:
    for y in computers[x]:
        if visited[y]:
            continue
        queue.append(y)
        visited[y] = 1
        res += 1
print(res)