import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nodes = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
queue = [(1, 0)]
visit = [0]*(n+1)
visit[1] = 1
for x, y in queue:
    for friend in nodes[x]:
        if not visit[friend] and y < 2:
            visit[friend] = 1
            queue.append((friend, y+1))
print(visit.count(1) - 1)